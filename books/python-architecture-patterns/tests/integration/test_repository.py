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


def test_repository_can_retrieve_a_batch_with_allocations(session):
    order_line = OrderLine(order_id="order1", sku="GENERIC-SOFA", quantity=10)
    batch = Batch(reference="batch1", sku="GENERIC-SOFA", purchased_quantity=100, eta=None, allocations=[order_line])

    repo = Repository(session)
    repo.add(batch)
    retrieved = repo.get("batch1")

    assert retrieved == batch
    assert retrieved.sku == batch.sku
    assert retrieved.purchased_quantity == batch.purchased_quantity
    assert retrieved.allocations == [order_line]
