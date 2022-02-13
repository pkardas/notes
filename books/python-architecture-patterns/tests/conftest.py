import time

import pytest
from sqlmodel import (
    Session,
    create_engine,
)
from starlette.testclient import TestClient

from src import config
from src.app import api
from src.domain.model import Batch
from src.adapters.orm import create_db_and_tables


@pytest.fixture
def in_memory_db():
    engine = create_engine("sqlite:///:memory:")
    create_db_and_tables(engine)
    return engine


@pytest.fixture
def session(in_memory_db):
    create_db_and_tables(in_memory_db)
    yield Session(in_memory_db)


def wait_for_postgres_to_come_up(engine):
    deadline = time.time() + 10
    while time.time() < deadline:
        try:
            return engine.connect()
        except Exception:
            time.sleep(0.5)
    pytest.fail("Postgres never came up")


def wait_for_webapp_to_come_up():
    deadline = time.time() + 10
    while time.time() < deadline:
        try:
            return TestClient(api).post("/allocate")
        except ConnectionError:
            time.sleep(0.5)
    pytest.fail("API never came up")


@pytest.fixture(scope="session")
def postgres_db():
    engine = create_engine(config.get_postgres_uri())
    wait_for_postgres_to_come_up(engine)
    create_db_and_tables(engine)
    return engine


@pytest.fixture
def postgres_session(postgres_db):
    create_db_and_tables(postgres_db)
    yield Session(postgres_db)


@pytest.fixture
def add_stock(postgres_session):
    batches = []

    def _add_stock(lines):
        for ref, sku, qty, eta in lines:
            batch = Batch(reference=ref, sku=sku, purchased_quantity=qty, eta=eta, allocations=[])
            postgres_session.add(batch)
            postgres_session.commit()
            batches.append(batch)

    yield _add_stock

    for batch in batches:
        postgres_session.delete(batch)
        postgres_session.commit()


@pytest.fixture
def client():
    return TestClient(api)
