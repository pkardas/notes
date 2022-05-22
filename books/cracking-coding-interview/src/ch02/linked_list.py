from typing import (
    List,
    Optional,
)

import pytest


class Node:
    def __init__(self, data: int) -> None:
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self, data: List[int]) -> None:
        self.head = None
        for val in data:
            self.append(val)

    @property
    def values(self) -> List[int]:
        result, current = [], self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def append(self, data: int) -> None:
        self.head = append(self.head, data)

    def delete(self, data: int) -> None:
        self.head = delete(self.head, data)


def delete(head: Optional[Node], data: int) -> Optional[Node]:
    node = head

    if not node:
        return None

    if head.data == data:
        return head.next

    while node.next:
        if node.next.data == data:
            node.next = node.next.next
            break
        node = node.next

    return head


def append(head: Optional[Node], data: int) -> Optional[Node]:
    if not head:
        return Node(data)

    current, end = head, Node(data)
    while current.next:
        current = current.next
    current.next = end

    return head


@pytest.mark.parametrize("values", [
    [],
    [1],
    [1, 2],
    [1, 2, 3],
])
def test_append(values):
    assert LinkedList(values).values == values


@pytest.mark.parametrize("values, to_delete, expected_result", [
    # @formatter:off
    ([],        0, []),
    ([1],       0, [1]),
    ([1],       1, []),
    ([1, 2],    1, [2]),
    ([1, 2],    2, [1]),
    ([1, 2, 3], 2, [1, 3]),
    # @formatter:on
])
def test_delete(values, to_delete, expected_result):
    linked_list = LinkedList(values)
    linked_list.delete(to_delete)
    assert linked_list.values == expected_result
