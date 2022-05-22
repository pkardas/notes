import pytest

from linked_list import LinkedList


def remove_duplicates_buffer(linked_list: LinkedList) -> LinkedList:
    unique_data = set()
    prev, current = None, linked_list.head

    while current:
        if current.data in unique_data:
            prev.next = current.next
        else:
            unique_data.add(current.data)
            prev = current
        current = current.next

    return linked_list


def remove_duplicates_no_buffer(linked_list: LinkedList) -> LinkedList:
    current = linked_list.head

    while current:
        runner = current

        while runner.next:
            if current.data == runner.next.data:
                runner.next = runner.next.next
            else:
                runner = runner.next

        current = current.next

    return linked_list


@pytest.mark.parametrize("values, expected_result", [
    # @formatter:off
    ([],           []),
    ([1, 1],       [1]),
    ([1, 1, 0],    [1, 0]),
    ([1, 1, 1, 1], [1]),
    ([0, 1, 0, 1], [0, 1]),
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    # @formatter:on
])
@pytest.mark.parametrize("function", [
    remove_duplicates_buffer,
    remove_duplicates_no_buffer
])
def test_algorithm(function, values, expected_result):
    linked_list = LinkedList(values)
    assert function(linked_list).values == expected_result
