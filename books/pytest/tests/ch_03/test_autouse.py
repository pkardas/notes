from time import (
    localtime,
    sleep,
    strftime,
    time,
)

import pytest


@pytest.fixture(scope="function")
def non_empty_db(cards_db, some_cards):
    for c in some_cards:
        cards_db.add_card(c)
    return cards_db


@pytest.fixture(autouse=True, scope="session")
def footer_session_scope():
    yield
    now = time()
    print("---")
    print(f"finished : {strftime('%d %b %X', localtime(now))}")
    print("--------")


@pytest.fixture(autouse=True)
def footer_function_scope():
    start = time()
    yield
    stop = time()
    print(f"test duration: {stop - start:0.3}")


def test_1():
    sleep(1)


def test_2():
    sleep(1.23)
