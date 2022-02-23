from threading import Thread
from time import sleep
from typing import List

import pytest
from sqlalchemy.orm import selectinload
from sqlmodel import (
    Session,
    select,
)

from src.domain.model import (
    Batch,
    OrderLine,
    Product,
)
from src.service_layer.unit_of_work import UnitOfWork
from tests.e2e.test_app import random_batch_ref

sku = "GENERIC-SOFA"


def insert_batch(session, batch_id):
    session.add(Product(sku=sku, batches=[Batch(reference=batch_id, sku=sku, purchased_quantity=100, eta=None)]))


def get_allocated_batch_ref(session, order_id, sku):
    batches = session.exec(select(Batch).where(Batch.sku == sku).options(selectinload(Batch.allocations))).all()
    batch = next(batch for batch in batches for allocation in batch.allocations if allocation.order_id == order_id)
    return batch.reference


def test_uow_retrieve_batch_and_allocate_to_it(session):
    insert_batch(session, "batch1")
    session.commit()

    with UnitOfWork(session) as uow:
        product = uow.products.get(sku=sku)
        line = OrderLine(order_id="o1", sku=sku, quantity=10)
        product.allocate(order_line=line)
        uow.commit()

    assert get_allocated_batch_ref(session, "o1", "GENERIC-SOFA") == "batch1"


def test_rolls_back_uncommitted_work_by_default(in_memory_db):
    old_session, new_session = Session(in_memory_db), Session(in_memory_db)
    with UnitOfWork():
        insert_batch(old_session, "batch1")
    assert list(new_session.exec(select(Batch)).all()) == []


def test_rolls_back_on_error(in_memory_db):
    old_session, new_session = Session(in_memory_db), Session(in_memory_db)

    class MyException(Exception):
        pass

    with pytest.raises(MyException):
        with UnitOfWork(old_session):
            insert_batch(old_session, "batch1")
            raise MyException()

    assert list(new_session.exec(select(Batch)).all()) == []


def try_to_allocate(order_id: str, exceptions: List[Exception]):
    line = OrderLine(order_id=order_id, sku=sku, quantity=10)
    try:
        with UnitOfWork() as uow:
            product = uow.products.get(sku)
            product.allocate(line)
            sleep(0.2)
            uow.commit()
    except Exception as e:
        exceptions.append(e)


def test_concurrent_updates_to_version_number_are_not_allowed(postgres_db):
    session = Session(postgres_db)
    insert_batch(session, random_batch_ref())
    session.commit()
    exceptions = []

    t1, t2 = Thread(target=try_to_allocate, args=("order_id_1", exceptions)), Thread(target=try_to_allocate, args=("order_id_2", exceptions))
    t1.start(), t2.start(), t1.join(), t2.join()

    product = session.exec(select(Product).where(Product.sku == sku)).one()
    assert product.version_number == 1
    assert "could not serialize access due to concurrent update" in str(exceptions[0])
