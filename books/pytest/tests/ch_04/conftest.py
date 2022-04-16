import pytest
from src import CardsDB


@pytest.fixture(scope="session")
def db(tmp_path_factory):
    db_path = tmp_path_factory.mktemp("cards_db")
    _db = CardsDB(db_path)
    yield _db
    _db.close()
