from __future__ import annotations


class Node:
    def __init__(self, val):
        self.val = val
        self.leafs = []

    def __str__(self):
        return self.val

    def add_child(self, val: Node):
        self.leafs.append(val)
