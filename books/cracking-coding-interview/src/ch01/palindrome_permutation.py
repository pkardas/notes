from collections import Counter

import pytest


def is_palindrome_permutation_pythonic(string: str) -> bool:
    raw_string = string.replace(' ', '')
    letter_frequency = Counter(raw_string)

    if len(raw_string) % 2 == 0:
        return all(frequency % 2 == 0 for frequency in letter_frequency.values())
    else:
        return sum(1 for frequency in letter_frequency.values() if frequency == 1) <= 1


def is_palindrome_permutation_counter(string: str) -> bool:
    raw_string = string.replace(' ', '')
    letter_frequency = Counter()
    num_of_odd = 0

    for ch in raw_string:
        letter_frequency[ch] += 1

        if letter_frequency[ch] % 2 == 1:
            num_of_odd += 1
        else:
            num_of_odd -= 1

    return num_of_odd <= 1


@pytest.mark.parametrize("string, expected_result", [
    # @formatter:off
    ("tact coa",     True),
    ("kamil slimak", True),
    ("slimakkamil ", True),
    ("aaaaaab",      True),
    ("aaa",          True),
    ("aaaaacb",      False),
    ("abc",          False),
    ("slimakoamil ", False),
    # @formatter:on
])
@pytest.mark.parametrize("function", [
    is_palindrome_permutation_pythonic,
    is_palindrome_permutation_counter
])
def test_algorithm(function, string, expected_result):
    assert function(string) == expected_result
