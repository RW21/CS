from unittest import TestCase
from algorithms.binary_tree_traversal import *
from data_structures import binary_tree

a = binary_tree.Node(1)
b = binary_tree.Node(2)
c = binary_tree.Node(3)
d = binary_tree.Node(4)
e = binary_tree.Node(5)
f = binary_tree.Node(6)
g = binary_tree.Node(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g


class TestBinaryTreeTraversal(TestCase):
    def test_in_order_traversal(self):
        order = []
        in_order_traversal(a, lambda x: order.append(x))
        self.assertEqual(order, [d, b, e, a, f, c, g])
