import pytest
import redis
from sqlmodel import (
    Session,
    create_engine,
)
from starlette.testclient import TestClient
from tenacity import (
    retry,
    stop_after_delay,
)

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


@retry(stop=stop_after_delay(10))
def wait_for_postgres_to_come_up(engine):
    engine.connect()


@retry(stop=stop_after_delay(10))
def wait_for_redis_to_come_up():
    r = redis.Redis(**config.get_redis_host_and_port())
    return r.ping()


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
