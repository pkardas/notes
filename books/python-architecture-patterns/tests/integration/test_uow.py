import pytest
from sqlalchemy.orm import selectinload
from sqlmodel import (
    Session,
    select,
)

from src.domain.model import (
    Batch,
    OrderLine,
)
from src.service_layer.unit_of_work import UnitOfWork


def insert_batch(session, batch_id):
    session.add(Batch(reference=batch_id, sku="GENERIC-SOFA", purchased_quantity=100, eta=None))


def get_allocated_batch_ref(session, order_id, sku):
    batches = session.exec(select(Batch).where(Batch.sku == sku).options(selectinload(Batch.allocations))).all()
    batch = next(batch for batch in batches for allocation in batch.allocations if allocation.order_id == order_id)
    return batch.reference


def test_uow_retrieve_batch_and_allocate_to_it(session):
    insert_batch(session, "batch1")
    session.commit()

    with UnitOfWork(session) as uow:
        batch = uow.batches.get(reference="batch1")
        line = OrderLine(order_id="o1", sku="GENERIC-SOFA", quantity=10)
        batch.allocate(order_line=line)
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
