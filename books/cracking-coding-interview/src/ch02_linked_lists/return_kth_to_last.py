from typing import Optional

import pytest

from linked_list import (
    LinkedList,
    Node,
)


def return_kth_to_last_simple(linked_list: LinkedList, k: int) -> int:
    node = linked_list.head
    position, i = len(linked_list.values) - k, 0

    if position < 0:
        return -1

    while node and i < position:
        node = node.next
        i += 1

    return node.data


def return_kth_to_last_simplest(linked_list: LinkedList, k: int) -> int:
    values = linked_list.values
    size = len(values)

    return values[size - k] if size - k >= 0 else -1


def return_kth_to_last_recursive(linked_list: LinkedList, k: int) -> int:
    found_value = None

    def _return_kth_to_last(node: Optional[Node]) -> int:
        if not node:
            return 0

        index = _return_kth_to_last(node.next) + 1

        if index == k:
            nonlocal found_value
            found_value = node.data

        return index

    _return_kth_to_last(linked_list.head)

    return found_value if found_value else -1


def return_kth_to_last_iterative(linked_list: LinkedList, k: int) -> int:
    p1, p2 = linked_list.head, linked_list.head

    for _ in range(k):
        if not p1:
            return -1
        p1 = p1.next

    while p1:
        p1 = p1.next
        p2 = p2.next

    return p2.data


@pytest.mark.parametrize("values, k, expected_result", [
    # @formatter:off
    ([1, 2, 3], 1, 3),
    ([1, 2, 3], 2, 2),
    ([1, 2, 3], 3, 1),
    ([1, 2, 3], 4, -1),
    # @formatter:on
])
@pytest.mark.parametrize("function", [
    return_kth_to_last_simple,
    return_kth_to_last_simplest,
    return_kth_to_last_recursive,
    return_kth_to_last_iterative,
])
def test_algorithm(function, values, k, expected_result):
    linked_list = LinkedList(values)
    assert function(linked_list, k) == expected_result
