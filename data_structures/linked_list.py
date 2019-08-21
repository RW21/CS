from __future__ import annotations


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        temp = self
        s = ["head: ", temp.val]
        while temp.next is not None:
            temp = self.next
            s.append(" -> ")
            s.append(temp.val)

        return "".join(s)

    def link(self, node: Node):
        self.next = node


# example
node_1 = Node('a')
node_2 = Node('b')

node_1.link(node_2)
print(node_1)
