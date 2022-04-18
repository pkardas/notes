import pytest

from src import (
    Card,
    CardsDB,
    InvalidCardId,
)

pytestmark = [pytest.mark.custom]

@pytest.fixture(scope="session")
def db(tmp_path_factory):
    db_path = tmp_path_factory.mktemp("cards_db")
    _db = CardsDB(db_path)
    yield _db
    _db.close()


@pytest.fixture(scope="function")
def cards_db(db):
    db.delete_all()
    return db


@pytest.mark.smoke
def test_start(cards_db):
    i = cards_db.add_card(Card("foo", state="todo"))
    cards_db.start(i)
    c = cards_db.get_card(i)
    assert c.state == "in prog"


@pytest.mark.exception
def test_start_non_existent(cards_db):
    with pytest.raises(InvalidCardId):
        cards_db.start(123)
