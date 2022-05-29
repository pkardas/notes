import pytest

from linked_list import (
    LinkedList,
    Node,
)


def is_palindrome_simple(linked_list: LinkedList) -> bool:
    values = linked_list.values
    return values == values[::-1]


def is_palindrome_reverse(linked_list: LinkedList) -> bool:
    def reverse_list() -> Node:
        head, node = None, linked_list.head

        while node:
            new_node = Node(data=node.data)
            new_node.next = head
            head = new_node

            node = node.next

        return head

    normal_node = linked_list.head
    reversed_node = reverse_list()

    while normal_node and reversed_node:
        if normal_node.data != reversed_node.data:
            return False
        normal_node = normal_node.next
        reversed_node = reversed_node.next

    return not normal_node and not reversed_node


def is_palindrome_slow_fast_runner(linked_list: LinkedList) -> bool:
    slow, fast = linked_list.head, linked_list.head
    stack = []

    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        if stack and stack.pop() != slow.data:
            return False
        slow = slow.next

    return True


@pytest.mark.parametrize("values, expected_result", [
    # @formatter:off
    ([1, 2, 3, 4], False),
    ([1, 2, 2, 2], False),
    ([1, 2, 2, 1], True),
    ([1, 2, 1],    True),
    ([1],          True),
    ([],           True)
    # @formatter:on
])
@pytest.mark.parametrize("function", [
    is_palindrome_simple,
    is_palindrome_reverse,
    is_palindrome_slow_fast_runner,
])
def test_algorithm(function, values, expected_result):
    linked_list = LinkedList(values)
    assert function(linked_list) == expected_result
