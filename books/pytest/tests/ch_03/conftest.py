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


@pytest.fixture(scope="session")
def some_cards():
    return [
        Card("write book", "brian", "done"),
        Card("edit book", "katie", "done"),
        Card("write 2nd edition", "brian", "todo"),
        Card("edit 2nd edition", "katie", "todo"),
    ]


