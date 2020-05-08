import collections


class Node:
    """
    Binary tree which can also generate from lists
    """
    def __init__(self, x):
        if type(x) == list:
            to_cut_power = 0
            to_cut_num = 2 ** to_cut_power
            layers = collections.defaultdict(list)

            for i, n in enumerate(x):
                if i >= to_cut_num:
                    to_cut_power += 1
                    to_cut_num = to_cut_num + 2 ** to_cut_power
                layers[to_cut_power].append(Node(n))

            # todo we don't really need to turn it into a dict

            for layer_depth in reversed(range(len(layers) - 1)):
                if (layer_depth + 1) in layers:
                    for mapping_count, node in enumerate(layers[layer_depth + 1]):
                        if mapping_count % 2 == 0:
                            layers[layer_depth][mapping_count // 2].left = node
                        else:
                            layers[layer_depth][mapping_count // 2].right = node

            try:
                self.val = layers[0][0].val
                self.right = layers[0][0].right
                self.left = layers[0][0].left
            except IndexError as e:
                print('Is the list filled?')
                print(e)

        else:

            self.val = x
            self.left = None
            self.right = None

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(self.val) + '(L:' + str(self.left) + ' R:' + str(self.right) + ')'

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
