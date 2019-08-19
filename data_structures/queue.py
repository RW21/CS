from data_structures.linked_list import Node


class Queue:
    def __init__(self):
        self.first: Node
        self.last: Node
        self.number_of_nodes = 0

    def __len__(self):
        return self.number_of_nodes

    def add(self, value):
        if self.number_of_nodes == 0:
            n = Node(value)
            self.last = n
            self.first = n

        else:
            self.last.link(Node(value))

        self.number_of_nodes += 1

    def remove(self):
        val = self.first.val
        self.first = self.first.next

        self.number_of_nodes -= 1
        return val

    def peek(self):
        return self.last.val


# example
q = Queue()
q.add('b')
q.add('c')
print(q.remove())
print(len(q))
print(q.remove())
