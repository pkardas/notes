from datetime import date
from unittest.mock import Mock

import pytest
from sqlmodel import Session

from src import views
from src.adapters.orm import clean_db_and_tables
from src.bootstrap import bootstrap
from src.domain import commands
from src.service_layer.unit_of_work import UnitOfWork

today = date.today()


@pytest.fixture
def sqlite_bus(in_memory_db):
    bus = bootstrap(
        start_orm=True,
        uow=UnitOfWork(Session(in_memory_db)),
        notifications=Mock(),
        publish=lambda *args: None,
    )
    yield bus
    clean_db_and_tables(in_memory_db)


def test_allocations_view(sqlite_bus):
    sqlite_bus.handle(commands.CreateBatch("sku1batch", "sku1", 50, None))
    sqlite_bus.handle(commands.CreateBatch("sku2batch", "sku2", 50, today))
    sqlite_bus.handle(commands.Allocate("order1", "sku1", 20))
    sqlite_bus.handle(commands.Allocate("order1", "sku2", 20))

    sqlite_bus.handle(commands.CreateBatch("sku1batch-later", "sku1", 50, today))
    sqlite_bus.handle(commands.Allocate("other_order", "sku1", 30))
    sqlite_bus.handle(commands.Allocate("other_order", "sku2", 10))

    assert views.allocations("order1", sqlite_bus.uow) == [
        {"sku": "sku1", "batch_ref": "sku1batch"},
        {"sku": "sku2", "batch_ref": "sku2batch"},
    ]


def test_deallocation(sqlite_bus):
    sqlite_bus.handle(commands.CreateBatch("b1", "sku1", 50, None))
    sqlite_bus.handle(commands.CreateBatch("b2", "sku1", 50, today))
    sqlite_bus.handle(commands.Allocate("o1", "sku1", 40))
    sqlite_bus.handle(commands.ChangeBatchQuantity("b1", 10))

    assert views.allocations("o1", sqlite_bus.uow) == [
        {"batch_ref": "b1", "sku": "sku1"},
        {"batch_ref": "b2", "sku": "sku1"}
    ]
