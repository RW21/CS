class GraphNode:
    def __init__(self, val):
        self.val = val
        self.adjacent = []

    def __str__(self):
        return str(self.val)

    def add_node(self, node):
        self.adjacent.append(node)

    def add_node_from_list(self, nodes: list):
        self.adjacent.extend(nodes)

