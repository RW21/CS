class Node:
    def __init__(self, val):
        self.val = val
        self.left_node = None
        self.right_node = None

# example
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)

node_1.left_node = node_2
node_1.right_node = node_3