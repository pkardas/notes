from datetime import date
from typing import (
    List,
    Optional,
)

from src.domain import model
from src.domain.model import (
    Batch,
    OrderLine,
)
from src.service_layer.unit_of_work import AbstractUnitOfWork


class InvalidSku(Exception):
    pass


def allocate(order_id: str, sku: str, quantity: int, uow: AbstractUnitOfWork) -> str:
    order_line = OrderLine(order_id=order_id, sku=sku, quantity=quantity)
    with uow:
        batches = uow.batches.list()

        if not is_valid_sku(sku, batches):
            raise InvalidSku(f"Invalid SKU: {sku}")

        batch_ref = model.allocate(order_line, batches)
        uow.commit()

    return batch_ref


def add_batch(ref: str, sku: str, quantity: int, eta: Optional[date], uow: AbstractUnitOfWork):
    with uow:
        uow.batches.add(Batch(reference=ref, sku=sku, purchased_quantity=quantity, eta=eta))
        uow.commit()


def is_valid_sku(sku: str, batches: List[Batch]):
    return sku in {batch.sku for batch in batches}
