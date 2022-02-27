from __future__ import annotations

from datetime import date
from typing import Optional
from unittest import mock

import pytest

from src.adapters.repository import (
    AbstractRepository,
    TrackingRepository,
)
from src.domain import events
from src.domain.model import Product
from src.service_layer import message_bus
from src.service_layer.handlers import InvalidSku
from src.service_layer.unit_of_work import AbstractUnitOfWork


class FakeRepository(AbstractRepository):
    def __init__(self, products):
        super().__init__()
        self._products = set(products)

    def add(self, product: Product):
        self._products.add(product)

    def get(self, sku: str) -> Optional[Product]:
        return next((product for product in self._products if product.sku == sku), None)

    def get_by_batch_ref(self, ref: str) -> Optional[Product]:
        return next((product for product in self._products for batch in product.batches if batch.reference == ref), None)


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.products = TrackingRepository(repo=FakeRepository([]))
        self.committed = False

    def rollback(self):
        pass

    def _commit(self):
        self.committed = True


class TestAddBatch:
    def test_for_new_product(self):
        uow = FakeUnitOfWork()
        message_bus.handle(events.BatchCreated(ref="b1", sku="CRUNCHY-ARMCHAIN", qty=100), uow)
        assert uow.products.get("CRUNCHY-ARMCHAIN") is not None
        assert uow.committed

    def test_for_existing_product(self):
        uow = FakeUnitOfWork()
        message_bus.handle(events.BatchCreated(ref="b1", sku="GARISH-RUG", qty=100), uow)
        message_bus.handle(events.BatchCreated(ref="b2", sku="GARISH-RUG", qty=99), uow)
        assert "b2" in [b.reference for b in uow.products.get("GARISH-RUG").batches]


class TestAllocate:
    def test_returns_allocation(self):
        uow = FakeUnitOfWork()
        message_bus.handle(events.BatchCreated(ref="batch1", sku="COMPLICATED-LAMP", qty=100), uow)
        [result] = message_bus.handle(events.AllocationRequired(order_id="o1", sku="COMPLICATED-LAMP", qty=10), uow)
        assert result == "batch1"

    def test_errors_for_invalid_sku(self):
        uow = FakeUnitOfWork()
        message_bus.handle(events.BatchCreated(ref="b1", sku="AREALSKU", qty=100), uow)
        with pytest.raises(InvalidSku, match="Invalid SKU: NONEXISTENTSKU"):
            message_bus.handle(events.AllocationRequired(order_id="o1", sku="NONEXISTENTSKU", qty=10), uow)

    def test_commits(self):
        uow = FakeUnitOfWork()
        message_bus.handle(events.BatchCreated(ref="b1", sku="OMINOUS-MIRROR", qty=100), uow)
        message_bus.handle(events.AllocationRequired(order_id="o1", sku="OMINOUS-MIRROR", qty=10), uow)
        assert uow.committed

    @mock.patch("src.adapters.email.send_mail")
    def test_sends_email_on_out_of_stock_error(self, mock_send_mail):
        uow = FakeUnitOfWork()
        message_bus.handle(events.BatchCreated(ref="b1", sku="POPULAR-CURTAINS", qty=9), uow)
        message_bus.handle(events.AllocationRequired(order_id="o1", sku="POPULAR-CURTAINS", qty=10), uow)
        assert mock_send_mail.call_args == mock.call("stock@made.com", "Out of stock for POPULAR-CURTAINS")


class TestChangeBatchQuantity:
    def test_changes_available_quantity(self):
        uow = FakeUnitOfWork()
        message_bus.handle(events.BatchCreated(ref="batch1", sku="ADORABLE-SETTEE", qty=100), uow)

        [batch] = uow.products.get("ADORABLE-SETTEE").batches
        assert batch.available_quantity == 100

        message_bus.handle(events.BatchQuantityChanged(ref="batch1", qty=50), uow)
        assert batch.available_quantity == 50

    def test_reallocates_if_necessary(self):
        uow = FakeUnitOfWork()
        event_history = [
            events.BatchCreated(ref="batch1", sku="INDIFFERENT-TABLE", qty=50),
            events.BatchCreated(ref="batch2", sku="INDIFFERENT-TABLE", qty=50, eta=date.today()),
            events.AllocationRequired(order_id="order1", sku="INDIFFERENT-TABLE", qty=20),
            events.AllocationRequired(order_id="order2", sku="INDIFFERENT-TABLE", qty=20),
        ]
        for e in event_history:
            message_bus.handle(e, uow)

        [batch_1, batch_2] = uow.products.get("INDIFFERENT-TABLE").batches
        assert batch_1.available_quantity == 10
        assert batch_2.available_quantity == 50

        message_bus.handle(events.BatchQuantityChanged(ref="batch1", qty=25), uow)
        assert batch_1.available_quantity == 5
        assert batch_2.available_quantity == 30
