import pytest


def check_if_has_unique_characters_pythonic(string: str) -> bool:
    return len(set(string)) == len(string)


def check_if_has_unique_characters_ascii(string: str) -> bool:
    boolean_array = [False] * 128
    for ch in string:
        int_ch = ord(ch)
        if boolean_array[int_ch]:
            return False
        boolean_array[int_ch] = True
    return True


def check_if_has_unique_characters_no_structures(string: str) -> bool:
    for i, ch_0 in enumerate(string):
        for ch_1 in string[i + 1:]:
            if ch_0 == ch_1:
                return False
    return True


def check_if_has_unique_characters_no_structures_sort(string: str) -> bool:
    sorted_string = sorted(string)

    for i in range(len(sorted_string) - 1):
        if sorted_string[i] == sorted_string[i + 1]:
            return False

    return True


@pytest.mark.parametrize("string, has_all_unique_chars", [
    # @formatter:off
    ("qwerty", True),
    ("",       True),
    ("qqwert", False),
    ("qwertt", False),
    # @formatter:on
])
@pytest.mark.parametrize("function", [
    check_if_has_unique_characters_pythonic,
    check_if_has_unique_characters_ascii,
    check_if_has_unique_characters_no_structures,
    check_if_has_unique_characters_no_structures_sort,
])
def test_algorithm(function, string, has_all_unique_chars):
    assert function(string) == has_all_unique_chars
