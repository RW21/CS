from data_structures import graph
from data_structures import queue as q


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
