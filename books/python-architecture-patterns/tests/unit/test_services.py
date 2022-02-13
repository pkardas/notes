import pytest
from sqlmodel import Session

from src.domain.model import (
    Batch,
    OrderLine,
)
from src.service_layer.services import (
    InvalidSku,
    allocate,
)
from src.adapters.repository import AbstractRepository


class FakeRepository(AbstractRepository):
    def __init__(self, batches):
        self._batches = set(batches)

    def add(self, batch):
        self._batches.add(batch)

    def get(self, reference):
        return next(b for b in self._batches if b.reference == reference)

    def list(self):
        return list(self._batches)


class FakeSession(Session):
    committed = False

    def commit(self):
        self.committed = True


def test_returns_allocation():
    line = OrderLine(order_id="o1", sku="COMPLICATED-LAMP", quantity=10)
    batch = Batch(reference="b1", sku="COMPLICATED-LAMP", purchased_quantity=100, eta=None)
    repo = FakeRepository([batch])

    result = allocate(line, repo, FakeSession())

    assert result == "b1"


def test_error_for_invalid_sku():
    line = OrderLine(order_id="o1", sku="NONEXISTENTSKU", quantity=10)
    batch = Batch(reference="b1", sku="AREALSKU", purchased_quantity=100, eta=None)
    repo = FakeRepository([batch])

    with pytest.raises(InvalidSku, match="Invalid SKU: NONEXISTENTSKU"):
        allocate(line, repo, FakeSession())


def test_commits():
    line = OrderLine(order_id="o1", sku="OMINOUS-MIRROR", quantity=10)
    batch = Batch(reference="b1", sku="OMINOUS-MIRROR", purchased_quantity=100, eta=None)
    repo = FakeRepository([batch])
    session = FakeSession()

    allocate(line, repo, session)

    assert session.committed
