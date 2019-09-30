from unittest import TestCase
from algorithms.binary_search import binary_search


class TestBinary_search(TestCase):
    def test_binary_search(self):
        assert binary_search([1, 5, 7, 9, 10], 5) == 1
