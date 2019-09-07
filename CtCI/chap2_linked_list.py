from data_structures.linked_list import Node


def remove_duplicate(head: Node):
    checked = set()
    new: Node = Node(None)
    new_ = new

    while True:

        if head.val not in checked:
            new.val = head.val
            checked.add(head.val)
        else:
            new.next = Node(None)
            new = new.next

        head = head.next

        if head.next is None:
            break
    return new_


def get_kth_to_last(head: Node, k: int) -> Node:
    slow, fast = head, head
    for i in range(k - 1):
        fast = fast.next

    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    return slow

