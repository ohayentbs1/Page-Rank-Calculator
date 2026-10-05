import unittest
from typing import List, Optional

class Page:
    def __init__(self, url: str = "", outgoing_pages: Optional[List['Page']] = None):
        self.url: str = url
        self.outgoing_pages: List['Page'] = outgoing_pages if outgoing_pages is not None else []
        self.incoming_pages: List['Page'] = []
        self.page_rank: float = 0.0
        self.last_page_rank: float = 0.0

    def add_outgoing_page(self, page: 'Page') -> None:
        if page not in self.outgoing_pages:
            self.outgoing_pages.append(page)

            if self not in page.incoming_pages:
                page.incoming_pages.append(self)

    def delete_outgoing_page(self, page: 'Page') -> None:
        if page in self.outgoing_pages:
            self.outgoing_pages.remove(page)
            if self in page.incoming_pages:
                page.incoming_pages.remove(self)

class Graph:
    def __init__(self, pages: Optional[List[Page]] = None, damping_factor: float = 0.85, max_iterations: int = 15):
        self.pages: List[Page] = pages if pages is not None else []
        self._damping_factor: float = damping_factor
        self._max_iterations: int = max_iterations

    def add_page(self, page: Page) -> None:
        if page not in self.pages:
            self.pages.append(page)

    def remove_page(self, page: Page) -> None:
        if page in self.pages:
            self.pages.remove(page)

            for p in self.pages:
                p.delete_outgoing_page(page)

    def calculate_page_rank(self) -> List[Page]:
        if len(self.pages) == 0:
            return self.pages

        for _ in range(self._max_iterations):

            for page in self.pages:
                page.last_page_rank = page.page_rank

            for page in self.pages:
                rank_sum = 0.0

                for incoming_page in page.incoming_pages:
                    out_degree = len(incoming_page.outgoing_pages)

                    if out_degree > 0:
                        rank_sum += (
                                incoming_page.last_page_rank / out_degree
                        )

                page.page_rank = (
                        (1.0 - self._damping_factor)
                        + self._damping_factor * rank_sum
                )

        return self.pages


class TestExampleGraph(unittest.TestCase):
    def test_page_ranks(self):
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
        page_ranks = {page.url: page.page_rank for page in results}

        self.assertAlmostEqual(page_ranks["https://example.com/a"], 0.2609, places=4)
        self.assertAlmostEqual(page_ranks["https://example.com/b"], 0.2609, places=4)
        self.assertAlmostEqual(page_ranks["https://example.com/c"], 0.3717, places=4)