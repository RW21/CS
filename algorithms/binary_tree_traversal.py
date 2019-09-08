from data_structures.binary_tree import Node as TreeNode


def in_order_traversal(node: TreeNode, visit):
    if node is not None:
        in_order_traversal(node.left, visit)
        visit(node)
        in_order_traversal(node.right, visit)


def pre_order_traversal(node: TreeNode, visit):
    if node is not None:
        visit(node)
        pre_order_traversal(node.left, visit)
        pre_order_traversal(node.right, visit)


def post_order_traversal(node: TreeNode, visit):
    if node is not None:
        post_order_traversal(node.left, visit)
        post_order_traversal(node.right, visit)
        visit(node)
