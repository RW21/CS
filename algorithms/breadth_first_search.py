from data_structures import graph
from data_structures import queue as q

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

def bfs(root: graph.GraphNode, visit):
    visited = set()
    visited.add(root)
    queue = q.Queue()
    queue.add(root)

    while queue:
        n: graph.GraphNode = queue.remove()
        visit(n)
        for node in n.adjacent:
            if node not in visited:
                visited.add(node)
                queue.add(node)
    return visited

bfs(a,print)