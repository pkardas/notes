import time
from pathlib import Path

import pytest
from sqlmodel import create_engine

from sqlmodel import Session
from starlette.testclient import TestClient

from src import config
from src.app import api
from src.model import Batch
from src.orm import create_db_and_tables


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
    def _add_stock(lines):
        for ref, sku, qty, eta in lines:
            postgres_session.add(Batch(reference=ref, sku=sku, purchased_quantity=qty, eta=eta, allocations=[]))
            postgres_session.commit()

    yield _add_stock


@pytest.fixture
def restart_api():
    time.sleep(0.5)
    wait_for_webapp_to_come_up()


@pytest.fixture
def client():
    return TestClient(api)
