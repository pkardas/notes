import time

import pytest
from sqlmodel import (
    Session,
    create_engine,
)
from starlette.testclient import TestClient

from src import config
from src.adapters.orm import (
    clean_db_and_tables,
    create_db_and_tables,
)
from src.app import api


@pytest.fixture
def in_memory_db():
    engine = create_engine("sqlite:///:memory:")
    clean_db_and_tables(engine)
    create_db_and_tables(engine)
    return engine


@pytest.fixture
def session(in_memory_db):
    create_db_and_tables(in_memory_db)
    yield Session(in_memory_db)
    clean_db_and_tables(in_memory_db)


def wait_for_postgres_to_come_up(engine):
    deadline = time.time() + 10
    while time.time() < deadline:
        try:
            return engine.connect()
        except Exception:
            time.sleep(0.5)
    pytest.fail("Postgres never came up")


@pytest.fixture(scope="session")
def postgres_db():
    engine = create_engine(config.get_postgres_uri())
    wait_for_postgres_to_come_up(engine)
    clean_db_and_tables(engine)
    create_db_and_tables(engine)
    return engine


@pytest.fixture
def postgres_session(postgres_db):
    create_db_and_tables(postgres_db)
    yield Session(postgres_db)
    clean_db_and_tables(postgres_db)


@pytest.fixture
def client():
    return TestClient(api)
