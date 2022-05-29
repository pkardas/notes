from typing import Optional

import pytest

from linked_list import (
    LinkedList,
    Node,
)


def get_loop(linked_list: LinkedList) -> Optional[Node]:
    slow, fast = linked_list.head, linked_list.head

    def get_loop_head():
        nonlocal slow, fast
        slow = linked_list.head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return get_loop_head()

    return None


l0 = LinkedList([1, 2, 3, 4, 5])
l0.node_for_value(5).next = l0.node_for_value(3)

l1 = LinkedList([1, 2, 3, 4, 5])


@pytest.mark.parametrize("linked_list, expected_result", [
    # @formatter:off
    (l0, l0.node_for_value(3)),
    (l1, None),
    # @formatter:on
])
def test_algorithm(linked_list, expected_result):
    assert get_loop(linked_list) == expected_result
