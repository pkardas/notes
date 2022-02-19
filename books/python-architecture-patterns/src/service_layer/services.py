from datetime import date
from typing import Optional

from src.domain.model import (
    Batch,
    OrderLine,
    Product,
)
from src.service_layer.unit_of_work import AbstractUnitOfWork


class InvalidSku(Exception):
    pass


def allocate(order_id: str, sku: str, quantity: int, uow: AbstractUnitOfWork) -> str:
    order_line = OrderLine(order_id=order_id, sku=sku, quantity=quantity)
    with uow:
        product = uow.products.get(sku=sku)

        if not product:
            raise InvalidSku(f"Invalid SKU: {sku}")

        batch_ref = product.allocate(order_line)
        uow.commit()

    return batch_ref


def add_batch(ref: str, sku: str, quantity: int, eta: Optional[date], uow: AbstractUnitOfWork):
    with uow:
        product = uow.products.get(sku)
        if not product:
            product = Product(sku=sku, batches=[])
            uow.products.add(product)
        product.batches.append(Batch(reference=ref, sku=sku, purchased_quantity=quantity, eta=eta))
        uow.commit()
