import pytest
from src import (
    Card,
    CardsDB,
)


@pytest.fixture(scope="session")
def db(tmp_path_factory):
    db_path = tmp_path_factory.mktemp("cards_db")
    _db = CardsDB(db_path)
    yield _db
    _db.close()


@pytest.fixture(scope="function")
def cards_db(db, request, faker):
    db.delete_all()

    faker.seed_instance(101)
    m = request.node.get_closest_marker("num_cards")
    if m and len(m.args) > 0:
        num_cards = m.args[0]
        for _ in range(num_cards):
            db.add_card(Card(summary=faker.sentence(), owner=faker.first_name()))
    return db


@pytest.mark.num_cards
def test_zero(cards_db):
    assert cards_db.count() == 0


@pytest.mark.num_cards(3)
def test_three(cards_db):
    assert cards_db.count() == 3
