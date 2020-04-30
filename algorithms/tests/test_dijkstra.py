from data_structures.graph import Graph, GraphNode, Edge

nodes = [GraphNode('e'), GraphNode('f'), GraphNode('c'), GraphNode('a'), GraphNode('b'), GraphNode('d')]
nodes = {n.val: n for n in nodes}

graph = Graph()

for node in nodes.values():
    graph.add_vertex(node)

edges = [Edge(nodes['e'], nodes['f'], 9), Edge(nodes['e'], nodes['d'], 6), Edge(nodes['f'], nodes['c'], 2),
         Edge(nodes['c'], nodes['d'], 11), Edge(nodes['f'], nodes['a'], 14), Edge(nodes['c'], nodes['a'], 9),
         Edge(nodes['c'], nodes['b'], 10), Edge(nodes['d'], nodes['b'], 15), Edge(nodes['a'], nodes['b'], 7)]

for edge in edges:
    graph.add_edge(edge)

print(graph)