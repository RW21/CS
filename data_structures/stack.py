class Stack:
    def __init__(self):
        self.list_: list = []
        self.max: int = 0
        
    def pop(self):
        if self.max == 0:
            raise EmptyException
        tmp = self.list_.pop(self.max - 1)
        self.max -= 1
        return tmp

    def push(self, item):
        self.list_.append(item)
        self.max += 1

    def peek(self):
        return self.list_[self.max] 

    def isEmpty(self):
        if max == 0:
            return True
        return False

class EmptyException(Exception):
    """
    Stack is empty.
    """

# example
s = Stack()
s.push('a')
s.push('b')
print(s.pop())
print(s.pop())
print(s.isEmpty())