import unittest
from classes import Page, Graph


class TestPage(unittest.TestCase):
    def setUp(self):
        self.p1 = Page(url="https://a.com")
        self.p2 = Page(url="https://b.com")

    def test_initialization(self):
        self.assertEqual(self.p1.url, "https://a.com")
        self.assertEqual(self.p1.outgoing_pages, [])
        self.assertEqual(self.p1.incoming_pages, [])
        self.assertEqual(self.p1.page_rank, 0.0)

    def test_add_outgoing_page(self):
        self.p1.add_outgoing_page(self.p2)

        self.assertIn(self.p2, self.p1.outgoing_pages)
        self.assertIn(self.p1, self.p2.incoming_pages)

    def test_delete_outgoing_page(self):
        self.p1.add_outgoing_page(self.p2)
        self.p1.delete_outgoing_page(self.p2)

        self.assertNotIn(self.p2, self.p1.outgoing_pages)
        self.assertNotIn(self.p1, self.p2.incoming_pages)


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.p1 = Page(url="https://a.com")
        self.p2 = Page(url="https://b.com")
        self.p3 = Page(url="https://c.com")
        self.graph = Graph()

    def test_add_and_remove_page(self):
        self.graph.add_page(self.p1)
        self.assertIn(self.p1, self.graph.pages)

        self.graph.remove_page(self.p1)
        self.assertNotIn(self.p1, self.graph.pages)

    def test_remove_page_cleans_up_references(self):
        # entfernen einer seite mit clean up bei der anderen
        self.graph.add_page(self.p1)
        self.graph.add_page(self.p2)
        self.p1.add_outgoing_page(self.p2)

        # p1 verweist auf p2 -> p2 entfernen
        self.graph.remove_page(self.p2)

        self.assertNotIn(self.p2, self.p1.outgoing_pages)

    def test_calculate_page_rank_single_page(self):
        self.graph.add_page(self.p1)
        self.graph.calculate_page_rank()

        # (1 - 0.85) + 0.85 * 0 = 0.15
        expected_rank = 1.0 - self.graph._damping_factor
        self.assertAlmostEqual(self.p1.page_rank, expected_rank, places=5)

    def test_calculate_page_rank_empty_graph(self):
        self.assertEqual(self.graph.calculate_page_rank(), [])

    def test_calculate_page_rank_linear_chain(self):
        # seiten in richtiger reihenfolge?
        self.graph.add_page(self.p1)
        self.graph.add_page(self.p2)
        self.graph.add_page(self.p3)

        self.p1.add_outgoing_page(self.p2)
        self.p2.add_outgoing_page(self.p3)

        self.graph.calculate_page_rank()
        self.assertGreater(self.p3.page_rank, self.p2.page_rank)
        self.assertGreater(self.p2.page_rank, self.p1.page_rank)


if __name__ == "__main__":
    unittest.main()