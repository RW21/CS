from data_structures.linked_list import Node


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.number_of_nodes = 0

    def __len__(self):
        return self.number_of_nodes

    def __str__(self):
        return str(self.first)

    def add(self, value):
        if self.last is not None:
            self.last.next = Node(value)
        self.last = Node(value)
        if self.first is None:
            self.first = self.last

        self.number_of_nodes += 1

    def remove(self):
        if self.first is None:
            raise QueueEmptyException
        else:
            val = self.first.val
            self.first = self.first.next
            if self.first is None:
                self.last = None
            self.number_of_nodes -= 1

        return val

    def peek(self):
        return self.last.val


class QueueEmptyException:
    """Queue is empty."""
