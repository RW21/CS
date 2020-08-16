class Node:
    """
    Binary tree which can also generate from lists
    """

    def __init__(self, x):
        if type(x) == list:
            def add(node, layer):
                if layer < len(x):
                    node.val = x[layer]
                    node.left = add(Node(None), layer * 2 + 1)
                    node.right = add(Node(None), layer * 2 + 2)
                return node

            add(self, 0)

        else:

            self.val = x
            self.left = None
            self.right = None

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        l, r = '', ''
        if self.left:
            l = self.left.val
        if self.right:
            r = self.right.val

        return str(self.val) + '(L:' + str(l) + ' R:' + str(r) + ')'

    def __len__(self):
        l_size, r_size = 0, 0
        if self.left:
            l_size = len(self.left)
        if self.right:
            r_size = len(self.right)

        if self.val is not None:
            return 1 + l_size + r_size
        else:
            return 0

    def __contains__(self, item):
        return self.val is not None and self.val == item or (item in self.right) or (item in self.left)

    def height(self, curr=0):
        l_height, r_height = curr, curr
        if self.left:
            l_height = self.left.height(curr=curr+1)
        if self.right:
            r_height = self.right.height(curr=curr+1)

        return max(l_height, r_height)

    def pretty_print(self):
        this_level = [self]
        while this_level:
            next_level = []
            for node in this_level:
                print(node.val, ' ', end=''),
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            print(" ")
            this_level = next_level


