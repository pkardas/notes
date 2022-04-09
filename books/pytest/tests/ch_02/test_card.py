import pytest

from src import Card


def test_field_access():
    c = Card("something", "brian", "todo", 123)
    assert (c.summary, c.owner, c.state, c.id) == ("something", "brian", "todo", 123)


def test_defaults():
    c = Card()
    assert (c.summary, c.owner, c.state, c.id) == (None, None, "todo", None)


def test_equality():
    assert Card("something", "brian", "todo", 123) == Card("something", "brian", "todo", 123)


def test_equality_with_different_ids():
    assert Card("something", "brian", "todo", 123) == Card("something", "brian", "todo", 321)


def test_inequality():
    assert Card("something", "brian", "todo", 123) != Card("completely different", "okken", "todo", 123)


def test_to_dict():
    assert Card.from_dict({
        "summary": "something",
        "owner": "brian",
        "state": "todo",
        "id": 123
    }) == Card("something", "brian", "todo", 123)


def test_from_dict():
    assert Card("something", "brian", "todo", 123).to_dict() == {
        "summary": "something",
        "owner": "brian",
        "state": "todo",
        "id": 123
    }
