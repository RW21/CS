from __future__ import annotations


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def link(self, node: Node):
        self.next = node

# example 
node_1 = Node('a')
node_2 = Node('b')

node_1.link(node_2)