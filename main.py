import os
import mysql.connector
from dotenv import load_dotenv
from classes import Graph, Page

load_dotenv()

con = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
)

try:
    cursor = con.cursor()
    try:
        cursor.execute("SELECT page_id, page_title FROM page")
        page_rows = cursor.fetchall()

        cursor.execute(
            """
            SELECT p_from.page_id, p_target.page_id
            FROM pagelinks AS pl
            JOIN page AS p_from
                ON p_from.page_id = pl.pl_from
            JOIN linktarget AS lt
                ON lt.lt_id = pl.pl_target_id
            JOIN page AS p_target
                ON p_target.page_namespace = lt.lt_namespace
                AND p_target.page_title = lt.lt_title
            """
        )
        link_rows = cursor.fetchall()
    finally:
        cursor.close()
finally:
    con.close()

pages = [
    Page(
        page_id=page_id,
        url=page_title.decode("utf-8") if isinstance(page_title, bytes) else page_title,
    )
    for page_id, page_title in page_rows
]
web_graph = Graph()
pages_by_id = {}
for page in pages:
    web_graph.add_page(page)
    pages_by_id[page.page_id] = page

for source_id, target_id in link_rows:
    source_page = pages_by_id.get(source_id)
    target_page = pages_by_id.get(target_id)
    if source_page is not None and target_page is not None:
        source_page.add_outgoing_page(target_page)

results = web_graph.calculate_page_rank()

print("Ergebnisse:")
for page in sorted(results, key=lambda p: p.page_rank, reverse=True):
    print(f"URL: {page.url:<22} | PageRank: {page.page_rank:.4f}")