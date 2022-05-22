import pytest


def check_permutation_sets(string: str, potential_permutation_string: str) -> bool:
    return len(string) == len(potential_permutation_string) and set(string) == set(potential_permutation_string)


def check_permutation_sort(string: str, potential_permutation_string: str) -> bool:
    return sorted(string) == sorted(potential_permutation_string)


def check_permutation_array(string: str, potential_permutation_string: str) -> bool:
    if len(string) != len(potential_permutation_string):
        return False

    url_array = [0] * 128

    for ch in string:
        url_array[ord(ch)] += 1

    for ch in potential_permutation_string:
        url_array[ord(ch)] -= 1

        if url_array[ord(ch)] < 0:
            return False

    return True


@pytest.mark.parametrize("string, potential_permutation_string, is_permutation", [
    # @formatter:off
    ("god",                 "dog",                 True),
    ("god",                 "dod",                 False),
    ("god",                 "dogg",                False),
    ("cat belongs to ala",  "ala belongs to cat",  True),
    ("interview questions", "interviews question", True),
    ("interview questions", "interview question",  False),
    # @formatter:on
])
@pytest.mark.parametrize("function", [
    check_permutation_sets,
    check_permutation_sort,
    check_permutation_array,
])
def test_algorithm(function, string, potential_permutation_string, is_permutation):
    assert function(string, potential_permutation_string) == is_permutation
