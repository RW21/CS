from unittest import TestCase
from data_structures import graph
from algorithms import breadth_first_search

a = graph.GraphNode(1)
b = graph.GraphNode(2)
c = graph.GraphNode(3)
d = graph.GraphNode(4)
e = graph.GraphNode(5)
f = graph.GraphNode(6)

a.add_nodes_from_list([b, e, f])
b.add_nodes_from_list([d, e])
c.add_node(b)
d.add_nodes_from_list([c, e])


class TestBfs(TestCase):
    def test_bfs(self):
        order = []
        assert breadth_first_search.bfs(a, lambda x: order.append(x)) == [a, b, e, f, d, c]
