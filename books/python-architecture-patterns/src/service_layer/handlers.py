from src.adapters import (
    email,
    redis_publisher,
)
from src.domain import (
    commands,
    events,
)

from src.domain.model import (
    Batch,
    OrderLine,
    Product,
)
from src.service_layer.unit_of_work import (
    AbstractUnitOfWork,
    UnitOfWork,
)


class InvalidSku(Exception):
    pass


def allocate(command: commands.Allocate, uow: AbstractUnitOfWork) -> str:
    order_line = OrderLine(order_id=command.order_id, sku=command.sku, qty=command.qty)
    with uow:
        product = uow.products.get(sku=command.sku)

        if not product:
            raise InvalidSku(f"Invalid SKU: {command.sku}")

        batch_ref = product.allocate(order_line)
        uow.commit()

    return batch_ref


def add_batch(command: commands.CreateBatch, uow: AbstractUnitOfWork):
    with uow:
        product = uow.products.get(command.sku)
        if not product:
            product = Product(sku=command.sku, batches=[])
            uow.products.add(product)
        product.batches.append(Batch(reference=command.ref, sku=command.sku, purchased_quantity=command.qty, eta=command.eta))
        uow.commit()


def change_batch_quantity(command: commands.ChangeBatchQuantity, uow: AbstractUnitOfWork):
    with uow:
        product = uow.products.get_by_batch_ref(command.ref)
        product.change_batch_quantity(ref=command.ref, qty=command.qty)
        uow.commit()


def send_out_of_stock_notification(event: events.OutOfStock, uow: AbstractUnitOfWork):
    email.send_mail("stock@made.com", f"Out of stock for {event.sku}")


def publish_allocated_event(event: events.Allocated, uow: AbstractUnitOfWork):
    redis_publisher.publish("line_allocated", event)


def add_allocation_to_read_model(event: events.Allocated, uow: UnitOfWork):
    with uow:
        uow.session.execute(
            """
            INSERT INTO allocationsview (order_id, sku, batch_ref)
            VALUES (:order_id, :sku, :batch_ref)
            """,
            dict(order_id=event.order_id, sku=event.sku, batch_ref=event.batch_ref),
        )
        uow.commit()


def remove_allocation_from_read_model(event: events.Deallocated, uow: UnitOfWork):
    with uow:
        uow.session.execute(
            """
            DELETE FROM allocationsview
            WHERE order_id = :order_id AND sku = :sku
            """,
            dict(order_id=event.order_id, sku=event.sku),
        )
        uow.commit()


def reallocate(event: events.Deallocated, uow: AbstractUnitOfWork, ):
    with uow:
        product = uow.products.get(sku=event.sku)
        product.messages.append(commands.Allocate(**event.dict()))
        uow.commit()
