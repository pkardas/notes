import pytest

from src import Card


def assert_identical(c1: Card, c2: Card):
    # Do not include 'assert_identical' in traceback:
    __tracebackhide__ = True

    assert c1 == c2
    if c1.id != c2.id:
        pytest.fail(f"id's don't match. {c1.id} != {c2.id}")


def test_identical():
    assert_identical(Card("foo", id=123), Card("foo", id=123))


@pytest.mark.skip()
def test_identical_fail():
    assert_identical(Card("foo", id=123), Card("foo", id=321))
