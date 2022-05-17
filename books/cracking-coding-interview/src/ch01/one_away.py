import pytest


def is_one_edit_away_pythonic(string: str, edit: str) -> bool:
    if abs(len(string) - len(edit)) > 1:
        return False

    if string in edit or edit in string:
        return True

    return len(set(string) - set(edit)) <= 1


def is_one_edit_away_loop(string: str, edit: str) -> bool:
    if abs(len(string) - len(edit)) > 1:
        return False

    shorter_text, longer_text = string if len(string) < len(edit) else edit, string if len(string) >= len(edit) else edit
    shorter_i, longer_i = 0, -1
    edit_found = False

    while shorter_i < len(shorter_text) and longer_i < len(longer_text):
        longer_i += 1

        if shorter_text[shorter_i] == longer_text[longer_i]:
            shorter_i += 1
            continue

        if edit_found:
            return False

        if len(string) == len(edit):
            shorter_i += 1

        edit_found = True

    return True


@pytest.mark.parametrize("string, edit, expected_result", [
    # @formatter:off
    ("pale",  "ple",  True),
    ("pale",  "ale",  True),
    ("ale",   "pale", True),
    ("pales", "pale", True),
    ("pale",  "bale", True),
    ("pale",  "bake", False),
    ("pale",  "ba",   False),
    # @formatter:on
])
@pytest.mark.parametrize("function", [
    is_one_edit_away_pythonic,
    is_one_edit_away_loop
])
def test_algorithm(function, string, edit, expected_result):
    assert function(string, edit) == expected_result
