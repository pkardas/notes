from src.domain.model import (
    Batch,
    OrderLine,
)
from src.adapters.repository import Repository


def test_repository_can_save_a_batch(session):
    batch = Batch(reference="batch1", sku="RUSTY-SOAPDISH", purchased_quantity=100, eta=None)

    repo = Repository(session)
    repo.add(batch)

    assert repo.list() == [Batch(reference="batch1", sku="RUSTY-SOAPDISH", eta=None, purchased_quantity=100, id=1)]


def insert_order_line(session):
    session.execute("INSERT INTO order_lines (orderid, sku, qty) VALUES ('order1', 'GENERIC-SOFA', 12)")
    [[orderline_id]] = session.execute(
        "SELECT id FROM order_lines WHERE orderid=:orderid AND sku=:sku",
        dict(orderid="order1", sku="GENERIC-SOFA"),
    )
    return orderline_id


def insert_batch(session, batch_id):
    session.execute(
        "INSERT INTO batches (reference, sku, _purchased_quantity, eta) VALUES (:batch_id, 'GENERIC-SOFA', 100, null)",
        dict(batch_id=batch_id),
    )
    [[batch_id]] = session.execute(
        'SELECT id FROM batches WHERE reference=:batch_id AND sku="GENERIC-SOFA"',
        dict(batch_id=batch_id),
    )
    return batch_id


def insert_allocation(session, order_id, batch_id):
    session.execute(
        "INSERT INTO allocations (order_id, batch_id) VALUES (:order_id, :batch_id)",
        dict(order_id=order_id, batch_id=batch_id),
    )


def test_repository_can_retrieve_a_batch_with_allocations(session):
    order_line = OrderLine(order_id="order1", sku="GENERIC-SOFA", quantity=10)
    batch = Batch(reference="batch1", sku="RUSTY-SOAPDISH", purchased_quantity=100, eta=None, allocations=[order_line])

    repo = Repository(session)
    repo.add(batch)
    retrieved = repo.get("batch1")

    assert retrieved == batch
    assert retrieved.sku == batch.sku
    assert retrieved.purchased_quantity == batch.purchased_quantity
    assert retrieved.allocations == [order_line]
