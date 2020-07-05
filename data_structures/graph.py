class GraphNode:
    def __init__(self, val):
        self.val = val
        self.adjacent = []

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()

    def add_node(self, node):
        self.adjacent.append(node)

    def add_nodes_from_list(self, nodes: list):
        self.adjacent.extend(nodes)


class Edge:
    def __init__(self, x: GraphNode, y: GraphNode, distance: int):
        self.x = x
        self.y = y
        self.distance = distance

    def reverse(self):
        return Edge(self.y, self.x, self.distance)

    def __repr__(self):
        return str(self.x) + '<-' + str(self.distance) + '->' + str(self.y)


class Graph:
    def __init__(self):
        self.vertexes = {}

    def __str__(self):
        return str(self.vertexes)

    def add_vertex(self, vertex):
        self.vertexes[vertex] = []

    def add_edge(self, edge: Edge):
        try:
            self.vertexes[edge.x].append(edge)
        except KeyError as e:
            print(str(edge.x) + 'not registered in graph')
            print(e)
        try:
            self.vertexes[edge.y].append(edge.reverse())
        except KeyError as e:
            print(str(edge.y) + 'not registered in graph')
            print(e)
