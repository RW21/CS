from __future__ import annotations


class Node:
    def __init__(self, val):
        # create from list
        if type(val) == list:
            s = self
            for i, node_val in enumerate(val):
                if i == 0:
                    s.val = node_val
                else:
                    s.link(Node(node_val))
                    s = s.next

        else:
            self.val = val
            self.next = None

    def __str__(self):
        temp = self
        s = ["head: ", str(temp.val)]
        while temp.next is not None:
            temp = temp.next
            s.append(" -> ")
            s.append(str(temp.val))

        return "".join(s)

    def link(self, node: Node):
        self.next = node

