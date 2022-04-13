import pytest


@pytest.fixture()
def some_data():
    return 42


def test_some_data(some_data):
    assert some_data == 42
