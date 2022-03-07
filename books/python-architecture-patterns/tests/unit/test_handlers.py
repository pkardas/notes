from __future__ import annotations

from collections import defaultdict
from datetime import date
from typing import (
    Dict,
    List,
    Optional,
)

import pytest

from src.adapters.notifications import AbstractNotifications
from src.adapters.repository import (
    AbstractRepository,
    TrackingRepository,
)
from src.bootstrap import bootstrap
from src.domain import commands
from src.domain.model import Product
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


class FakeNotifications(AbstractNotifications):
    def __init__(self):
        self.sent: Dict[str, List[str]] = defaultdict(list)

    def send(self, destination, message):
        self.sent[destination].append(message)


def bootstrap_test_app():
    return bootstrap(
        start_orm=False,
        uow=FakeUnitOfWork(),
        notifications=FakeNotifications(),
        publish=lambda *args: None,
    )


class TestAddBatch:
    def test_for_new_product(self):
        bus = bootstrap_test_app()
        bus.handle(commands.CreateBatch(ref="b1", sku="CRUNCHY-ARMCHAIN", qty=100))
        assert bus.uow.products.get("CRUNCHY-ARMCHAIN") is not None
        assert bus.uow.committed

    def test_for_existing_product(self):
        bus = bootstrap_test_app()
        bus.handle(commands.CreateBatch(ref="b1", sku="GARISH-RUG", qty=100))
        bus.handle(commands.CreateBatch(ref="b2", sku="GARISH-RUG", qty=99))
        assert "b2" in [b.reference for b in bus.uow.products.get("GARISH-RUG").batches]


class TestAllocate:
    def test_errors_for_invalid_sku(self):
        bus = bootstrap_test_app()
        bus.handle(commands.CreateBatch(ref="b1", sku="AREALSKU", qty=100))
        with pytest.raises(InvalidSku, match="Invalid SKU: NONEXISTENTSKU"):
            bus.handle(commands.Allocate(order_id="o1", sku="NONEXISTENTSKU", qty=10))

    def test_commits(self):
        bus = bootstrap_test_app()
        bus.handle(commands.CreateBatch(ref="b1", sku="OMINOUS-MIRROR", qty=100))
        bus.handle(commands.Allocate(order_id="o1", sku="OMINOUS-MIRROR", qty=10))
        assert bus.uow.committed

    def test_sends_email_on_out_of_stock_error(self):
        fake_notifications = FakeNotifications()
        bus = bootstrap(
            start_orm=False,
            uow=FakeUnitOfWork(),
            notifications=fake_notifications,
            publish=lambda *args: None,
        )
        bus.handle(commands.CreateBatch(ref="b1", sku="POPULAR-CURTAINS", qty=9))
        bus.handle(commands.Allocate(order_id="o1", sku="POPULAR-CURTAINS", qty=10))
        assert fake_notifications.sent["stock@made.com"] == ["Out of stock for POPULAR-CURTAINS"]


class TestChangeBatchQuantity:
    def test_changes_available_quantity(self):
        bus = bootstrap_test_app()
        bus.handle(commands.CreateBatch(ref="batch1", sku="ADORABLE-SETTEE", qty=100))

        [batch] = bus.uow.products.get("ADORABLE-SETTEE").batches
        assert batch.available_quantity == 100

        bus.handle(commands.ChangeBatchQuantity(ref="batch1", qty=50))
        assert batch.available_quantity == 50

    def test_reallocates_if_necessary(self):
        bus = bootstrap_test_app()
        event_history = [
            commands.CreateBatch(ref="batch1", sku="INDIFFERENT-TABLE", qty=50),
            commands.CreateBatch(ref="batch2", sku="INDIFFERENT-TABLE", qty=50, eta=date.today()),
            commands.Allocate(order_id="order1", sku="INDIFFERENT-TABLE", qty=20),
            commands.Allocate(order_id="order2", sku="INDIFFERENT-TABLE", qty=20),
        ]
        for e in event_history:
            bus.handle(e)

        [batch_1, batch_2] = bus.uow.products.get("INDIFFERENT-TABLE").batches
        assert batch_1.available_quantity == 10
        assert batch_2.available_quantity == 50

        bus.handle(commands.ChangeBatchQuantity(ref="batch1", qty=25))
        assert batch_1.available_quantity == 5
        assert batch_2.available_quantity == 30
