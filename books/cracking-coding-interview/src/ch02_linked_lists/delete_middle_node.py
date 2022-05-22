import pytest

from linked_list import (
    LinkedList,
    Node,
)


def delete_middle_node(node: Node) -> None:
    assert node.next, "node is not the last node in the linked list"

    node.data = node.next.data
    node.next = node.next.next


@pytest.mark.parametrize("values, node, expected_result", [
    # @formatter:off
    ([1, 2, 3, 4], 2, [1, 3, 4]),
    ([1, 2, 3, 4], 3, [1, 2, 4]),
    # @formatter:on
])
def test_algorithm(values, node, expected_result):
    linked_list = LinkedList(values)
    delete_middle_node(linked_list.node_for_value(node))
    assert linked_list.values == expected_result
