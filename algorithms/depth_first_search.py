from data_structures import graph
from data_structures import stack as s

def dfs(root: graph.GraphNode, visit):
    visited = set()
    visited.add(root)
    stack = s.Stack()
    stack.push(root)

    while stack:
        n: graph.GraphNode = stack.pop()
        if n not in visited:
            visited.add(n)
            for neighbor in n.adjacent:
                stack.push(neighbor)