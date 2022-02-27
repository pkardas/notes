from src.adapters import email
from src.domain import events

from src.domain.model import (
    Batch,
    OrderLine,
    Product,
)
from src.service_layer.unit_of_work import AbstractUnitOfWork


class InvalidSku(Exception):
    pass


def allocate(event: events.AllocationRequired, uow: AbstractUnitOfWork) -> str:
    order_line = OrderLine(order_id=event.order_id, sku=event.sku, qty=event.qty)
    with uow:
        product = uow.products.get(sku=event.sku)

        if not product:
            raise InvalidSku(f"Invalid SKU: {event.sku}")

        batch_ref = product.allocate(order_line)
        uow.commit()

    return batch_ref


def add_batch(event: events.BatchCreated, uow: AbstractUnitOfWork):
    with uow:
        product = uow.products.get(event.sku)
        if not product:
            product = Product(sku=event.sku, batches=[])
            uow.products.add(product)
        product.batches.append(Batch(reference=event.ref, sku=event.sku, purchased_quantity=event.qty, eta=event.eta))
        uow.commit()


def change_batch_quantity(event: events.BatchQuantityChanged, uow: AbstractUnitOfWork):
    with uow:
        product = uow.products.get_by_batch_ref(event.ref)
        product.change_batch_quantity(ref=event.ref, qty=event.qty)
        uow.commit()


def send_out_of_stock_notification(event: events.OutOfStock, uow: AbstractUnitOfWork):
    email.send_mail("stock@made.com", f"Out of stock for {event.sku}")
