from dataclasses import dataclass

import pytest


def compress_string(text: str) -> str:
    @dataclass
    class Compressed:
        char: str
        freq: int

    compressed = []

    for ch in text:
        if compressed and ch == compressed[-1].char:
            compressed[-1].freq += 1
        else:
            compressed.append(Compressed(char=ch, freq=1))

    return ''.join(f"{c.char}{c.freq}" for c in compressed) if len(compressed) * 2 < len(text) else text


@pytest.mark.parametrize("text, expected_result", [
    # @formatter:off
    ("a",       "a"),
    ("aabb",    "aabb"),
    ("aaaa",    "a4"),
    ("aabbb",   "a2b3"),
    ("aabbbaa", "a2b3a2"),
    # @formatter:on
])
def test_algorithm(text, expected_result):
    assert compress_string(text) == expected_result
