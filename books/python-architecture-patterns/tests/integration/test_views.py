from datetime import date

from src import views
from src.domain import commands
from src.service_layer import message_bus
from src.service_layer.unit_of_work import UnitOfWork

today = date.today()


def test_allocations_view(session):
    uow = UnitOfWork(session)
    message_bus.handle(commands.CreateBatch("sku1batch", "sku1", 50, None), uow)
    message_bus.handle(commands.CreateBatch("sku2batch", "sku2", 50, today), uow)
    message_bus.handle(commands.Allocate("order1", "sku1", 20), uow)
    message_bus.handle(commands.Allocate("order1", "sku2", 20), uow)

    message_bus.handle(commands.CreateBatch("sku1batch-later", "sku1", 50, today), uow)
    message_bus.handle(commands.Allocate("other_order", "sku1", 30), uow)
    message_bus.handle(commands.Allocate("other_order", "sku2", 10), uow)

    assert views.allocations("order1", uow) == [
        {"sku": "sku1", "batch_ref": "sku1batch"},
        {"sku": "sku2", "batch_ref": "sku2batch"},
    ]


def test_deallocation(session):
    uow = UnitOfWork(session)
    message_bus.handle(commands.CreateBatch("b1", "sku1", 50, None), uow)
    message_bus.handle(commands.CreateBatch("b2", "sku1", 50, today), uow)
    message_bus.handle(commands.Allocate("o1", "sku1", 40), uow)
    message_bus.handle(commands.ChangeBatchQuantity("b1", 10), uow)

    assert views.allocations("o1", uow) == [
        {"batch_ref": "b1", "sku": "sku1"},
        {"batch_ref": "b2", "sku": "sku1"}
    ]
