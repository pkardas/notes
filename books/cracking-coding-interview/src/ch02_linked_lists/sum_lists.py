import pytest

from linked_list import (
    LinkedList,
    Node,
)


def sum_lists(list_0: LinkedList, list_1: LinkedList) -> LinkedList:
    result, remainder = [], 0
    node_0, node_1 = list_0.head, list_1.head

    def add_aligned_lists() -> None:
        nonlocal node_0, node_1, result, remainder
        while node_0 and node_1:
            result.append((node_0.data + node_1.data + remainder) % 10)
            remainder = 1 if (node_0.data + node_1.data + remainder) >= 10 else 0
            node_0, node_1 = node_0.next, node_1.next

    def align_remaining_list(node: Node) -> None:
        nonlocal result, remainder
        while node:
            result.append((node.data + remainder) % 10)
            remainder = 1 if (node.data + remainder) >= 10 else 0
            node = node.next

    add_aligned_lists()
    align_remaining_list(node_0)
    align_remaining_list(node_1)

    if remainder:
        result.append(remainder)

    return LinkedList(result)


@pytest.mark.parametrize("list_0, list_1, expected_result", [
    # @formatter:off
    ([7, 1, 6], [5, 9, 2], [2, 1, 9]),
    ([1, 7, 1], [3],       [4, 7, 1]),
    ([9, 9, 9], [1],       [0, 0, 0, 1]),
    ([7, 1],    [3, 1],    [0, 3]),
    ([7, 1],    [3],       [0, 2]),
    # @formatter:on
])
def test_algorithm(list_0, list_1, expected_result):
    list_0, list_1 = LinkedList(list_0), LinkedList(list_1)
    assert sum_lists(list_0, list_1).values == expected_result
