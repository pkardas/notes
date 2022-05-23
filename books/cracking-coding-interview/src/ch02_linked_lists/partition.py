from typing import Tuple

import pytest
from linked_list import LinkedList


def partition(linked_list: LinkedList, partition_val: int) -> Tuple[LinkedList, LinkedList]:
    l1, l2 = LinkedList(data=[]), LinkedList(data=[])
    node = linked_list.head

    while node:
        if node.data < partition_val:
            l1.append(node.data)
        else:
            l2.append(node.data)
        node = node.next

    return l1, l2


@pytest.mark.parametrize("values, partition_val, expected_values", [
    # @formatter:off
    ([1, 2, 3, 4, 5], 3, ([1, 2],          [3, 4, 5])),
    ([1, 2, 3, 4, 5], 0, ([],              [1, 2, 3, 4, 5])),
    ([1, 2, 3, 4, 5], 6, ([1, 2, 3, 4, 5], [])),
    # @formatter:on
])
def test_algorithm(values, partition_val, expected_values):
    linked_list = LinkedList(values)
    l1, l2 = partition(linked_list, partition_val)
    assert (l1.values, l2.values) == expected_values
