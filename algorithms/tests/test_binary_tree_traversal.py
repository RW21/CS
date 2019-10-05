from unittest import TestCase
from algorithms.binary_tree_traversal import *
from data_structures.binary_tree import Node

root = Node(1)
left = Node(2)
right = Node(3)
left_left = Node(4)
left_right = Node(5)
right_left = Node(6)
right_right = Node(7)
root.left = left
root.right = right
left.left = left_left
left.right = left_right
right.left = right_left
right.right = right_right


class TestBinary_search(TestCase):
    def test_in_order_traversal(self):
        order = []
        in_order_traversal(root, lambda x: order.append(x.val))
        assert order == [4, 2, 5, 1, 6, 3, 7]

    def test_pre_order_traversal(self):
        order = []
        pre_order_traversal(root, lambda x: order.append(x.val))
        assert order == [1, 2, 4, 5, 3, 6, 7]

    def test_post_order_traversal(self):
        order = []
        post_order_traversal(root, lambda x: order.append(x.val))
        assert order == [4, 5, 2, 6, 7, 3, 1]
