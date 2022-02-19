from __future__ import annotations

from datetime import datetime
from typing import Optional

import pytest

from src.adapters.repository import AbstractRepository
from src.domain.model import Batch
from src.service_layer.services import (
    InvalidSku,
    add_batch,
    allocate,
)
from src.service_layer.unit_of_work import AbstractUnitOfWork


class FakeRepository(AbstractRepository):
    def __init__(self, batches):
        self._batches = set(batches)

    @staticmethod
    def for_batch(ref: str, sku: str, quantity: int, eta: Optional[datetime] = None) -> FakeRepository:
        return FakeRepository([Batch(reference=ref, sku=sku, purchased_quantity=quantity, eta=eta)])

    def add(self, batch):
        self._batches.add(batch)

    def get(self, reference):
        return next(b for b in self._batches if b.reference == reference)

    def list(self):
        return list(self._batches)


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.batches = FakeRepository([])
        self.committed = False

    def commit(self):
        self.committed = True

    def rollback(self):
        pass


def test_add_batch():
    uow = FakeUnitOfWork()
    add_batch("b1", "CRUNCHY-ARMCHAIN", 100, None, uow)
    assert uow.batches.get("b1") is not None
    assert uow.committed


def test_allocate_returns_allocation():
    uow = FakeUnitOfWork()
    add_batch("batch1", "COMPLICATED-LAMP", 100, None, uow)
    result = allocate("o1", "COMPLICATED-LAMP", 10, uow)
    assert result == "batch1"


def test_allocate_errors_for_invalid_sku():
    uow = FakeUnitOfWork()
    add_batch("b1", "AREALSKU", 100, None, uow)
    with pytest.raises(InvalidSku, match="Invalid SKU: NONEXISTENTSKU"):
        allocate("o1", "NONEXISTENTSKU", 10, uow)


def test_commits():
    uow = FakeUnitOfWork()
    add_batch("b1", "OMINOUS-MIRROR", 100, None, uow)
    allocate("o1", "OMINOUS-MIRROR", 10, uow)
    assert uow.committed
