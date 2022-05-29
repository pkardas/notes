from typing import Optional

import pytest

from linked_list import (
    LinkedList,
    Node,
)


def intersection(list_0: LinkedList, list_1: LinkedList) -> Optional[Node]:
    if list_0.tail != list_1.tail:
        return None

    l0_node, l1_node = list_0.head, list_1.head
    l0_len, l1_len = list_0.length, list_1.length

    # Advance pointers when lists have different size:
    if l0_len > l1_len:
        for i in range(l0_len - l1_len):
            l0_node = l0_node.next

    if l0_len < l1_len:
        for i in range(l1_len - l0_len):
            l1_len = l1_len.next

    while l0_node and l1_node:
        if l0_node == l1_node:
            return l0_node
        l0_node = l0_node.next
        l1_node = l1_node.next

    assert False, "Loop above must finish the program"


l0 = LinkedList([3, 1, 5, 9])
l1 = LinkedList([4, 6])
tail = LinkedList([7, 2, 1]).head

l4 = LinkedList([3, 1, 5, 9, 7, 2, 1])
l5 = LinkedList([4, 6, 7, 2, 1])


@pytest.mark.parametrize("list_0, list_0_tail, list_1, list_1_tail, expected_result", [
    # @formatter:off
    (l0, tail, l1, tail, tail),
    (l4, None, l5, None, None)
    # @formatter:on
])
def test_algorithm(list_0, list_0_tail, list_1, list_1_tail, expected_result):
    list_0.tail.next = list_0_tail
    list_1.tail.next = list_1_tail

    assert intersection(list_0, list_1) == expected_result
