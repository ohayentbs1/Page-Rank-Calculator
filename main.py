from classes import *
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

con = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
)

con.close()

page_a = Page(url="https://example.com/a")
page_b = Page(url="https://example.com/b")
page_c = Page(url="https://example.com/c")

page_a.add_outgoing_page(page_b)
page_a.add_outgoing_page(page_c)
page_b.add_outgoing_page(page_a)
page_b.add_outgoing_page(page_c)

web_graph = Graph(damping_factor=0.85, max_iterations=15)
web_graph.add_page(page_a)
web_graph.add_page(page_b)
web_graph.add_page(page_c)

results = web_graph.calculate_page_rank()

print("Ergebnisse:")
for page in sorted(results, key=lambda p: p.page_rank, reverse=True):
    print(f"URL: {page.url:<22} | PageRank: {page.page_rank:.4f}")