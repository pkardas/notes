from __future__ import annotations

from typing import Optional

import pytest

from src.adapters.repository import (
    AbstractRepository,
    TrackingRepository,
)
from src.domain.model import Product
from src.service_layer.services import (
    InvalidSku,
    add_batch,
    allocate,
)
from src.service_layer.unit_of_work import AbstractUnitOfWork


class FakeRepository(AbstractRepository):
    def __init__(self, products):
        super().__init__()
        self._products = set(products)

    def add(self, product: Product):
        self._products.add(product)

    def get(self, sku: str) -> Optional[Product]:
        return next((product for product in self._products if product.sku == sku), None)


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.products = TrackingRepository(repo=FakeRepository([]))
        self.committed = False

    def rollback(self):
        pass

    def _commit(self):
        self.committed = True


def test_add_batch():
    uow = FakeUnitOfWork()
    add_batch("b1", "CRUNCHY-ARMCHAIN", 100, None, uow)
    assert uow.products.get("CRUNCHY-ARMCHAIN") is not None
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
