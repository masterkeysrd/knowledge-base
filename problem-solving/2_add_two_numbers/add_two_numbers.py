class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        if self.next:
            return f"ListNode({self.val}, {repr(self.next)})"
        else:
            return f"ListNode({self.val})"


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """Return the sum of two numbers represented by linked lists.

    Args:
        l1 (ListNode): Head of the first linked list.
        l2 (ListNode): Head of the second linked list.

    Returns:
        ListNode: Head of the resulting linked list.

    Examples:
        >>> l1 = ListNode(2, ListNode(4, ListNode(3)))
        >>> l2 = ListNode(5, ListNode(6, ListNode(4)))
        >>> add_two_numbers(l1, l2)
        ListNode(7, ListNode(0, ListNode(8)))
        >>> l1 = ListNode(0)
        >>> l2 = ListNode(0)
        >>> add_two_numbers(l1, l2)
        ListNode(0)
        >>> l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
        >>> l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
        >>> add_two_numbers(l1, l2)
        ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))))))
    """
    result = ListNode(0)

    current_result_list = result
    current_list1 = l1
    current_list2 = l2

    while current_list1 or current_list2:
        value = current_result_list.val

        if current_list1:
            value = value + current_list1.val
            current_list1 = current_list1.next

        if current_list2:
            value = value + current_list2.val
            current_list2 = current_list2.next

        add_to_next = value // 10
        current_result_list.val = value % 10

        if current_list1 or current_list2 or add_to_next:
            current_result_list.next = ListNode(add_to_next)
            current_result_list = current_result_list.next

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # [7, 0, 8]
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    # [5, 6, 4]
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    print(add_two_numbers(l1, l2))

    # [0]
    l1 = ListNode(0)
    # [0]
    l2 = ListNode(0)
    print(add_two_numbers(l1, l2))

    # [9, 9, 9, 9, 9, 9, 9]
    l1 = ListNode(9, ListNode(9, ListNode(
        9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    # [9, 9, 9, 9]
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    print(add_two_numbers(l1, l2))

# Output:
# ListNode(7, ListNode(0, ListNode(8)))
# ListNode(0)
# ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))))))
