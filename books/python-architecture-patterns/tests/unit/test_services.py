from __future__ import annotations

from datetime import datetime
from typing import Optional

import pytest
from sqlmodel import Session

from src.adapters.repository import AbstractRepository
from src.domain.model import Batch
from src.service_layer.services import (
    InvalidSku,
    add_batch,
    allocate,
)


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


class FakeSession(Session):
    committed = False

    def commit(self):
        self.committed = True


def test_add_batch():
    repo, session = FakeRepository([]), FakeSession()

    add_batch("b1", "CRUNCHY-ARMCHAIN", 100, None, repo, session)

    assert repo.get("b1") is not None
    assert session.committed


def test_allocate_returns_allocation():
    repo, session = FakeRepository([]), FakeSession()
    add_batch("batch1", "COMPLICATED-LAMP", 100, None, repo, session)

    result = allocate("o1", "COMPLICATED-LAMP", 10, repo, session)

    assert result == "batch1"


def test_allocate_errors_for_invalid_sku():
    repo, session = FakeRepository([]), FakeSession()
    add_batch("b1", "AREALSKU", 100, None, repo, session)

    with pytest.raises(InvalidSku, match="Invalid SKU: NONEXISTENTSKU"):
        allocate("o1", "NONEXISTENTSKU", 10, repo, FakeSession())


def test_commits():
    repo, session = FakeRepository([]), FakeSession()

    add_batch("b1", "OMINOUS-MIRROR", 100, None, repo, session)
    allocate("o1", "OMINOUS-MIRROR", 10, repo, session)

    assert session.committed
