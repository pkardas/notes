from datetime import date
from typing import (
    List,
    Optional,
)

from sqlmodel import Session

from src.adapters.repository import AbstractRepository
from src.domain import model
from src.domain.model import (
    Batch,
    OrderLine,
)


class InvalidSku(Exception):
    pass


def allocate(order_id: str, sku: str, quantity: int, repo: AbstractRepository, session: Session) -> str:
    batches = repo.list()
    order_line = OrderLine(order_id=order_id, sku=sku, quantity=quantity)

    if not is_valid_sku(sku, batches):
        raise InvalidSku(f"Invalid SKU: {sku}")

    batch_ref = model.allocate(order_line, batches)
    session.commit()

    return batch_ref


def add_batch(ref: str, sku: str, quantity: int, eta: Optional[date], repo: AbstractRepository, session: Session):
    repo.add(Batch(reference=ref, sku=sku, purchased_quantity=quantity, eta=eta))
    session.commit()


def is_valid_sku(sku: str, batches: List[Batch]):
    return sku in {batch.sku for batch in batches}
