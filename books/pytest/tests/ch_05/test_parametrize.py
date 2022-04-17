from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from src import (
    Card,
    CardsDB,
)


@pytest.fixture(scope="session")
def db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        _db = CardsDB(db_path)
        yield _db
        _db.close()


@pytest.fixture(scope="function")
def cards_db(db):
    db.delete_all()
    return db


@pytest.mark.parametrize("initial_state", ["done", "in prog", "todo"])
def test_finish(cards_db, initial_state):
    c = Card("write a book", state=initial_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)

    c = cards_db.get_card(index)

    assert c.state == "done"


@pytest.fixture(params=["done", "in prog", "todo"])
def start_state(request):
    return request.param


def test_finish_v2(cards_db, start_state):
    c = Card("write a book", state=start_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)

    c = cards_db.get_card(index)

    assert c.state == "done"


def pytest_generate_tests(metafunc):
    if "start_state_2" in metafunc.fixturenames:
        metafunc.parametrize("start_state_2", ["done", "in prog", "todo"])


def test_finish_v3(cards_db, start_state_2):
    c = Card("write a book", state=start_state_2)
    index = cards_db.add_card(c)
    cards_db.finish(index)

    c = cards_db.get_card(index)

    assert c.state == "done"