import pytest


def is_rotated(string: str, rotated_string: str) -> bool:
    return len(string) == len(rotated_string) and rotated_string in string * 2


@pytest.mark.parametrize("string, rotated_string, expected_result", [
    # @formatter:off
    ("",            "",            True),
    ("waterbottle", "erbottlewat", True),
    ("dog",         "gdo",         True),
    ("dog",         "dogdo",       False),
    ("dog",         "godd",        False),
    ("dog",         "go",          False),
    # @formatter:on
])
def test_algorithm(string, rotated_string, expected_result):
    assert is_rotated(string, rotated_string) == expected_result
