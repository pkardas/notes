from typing import List

from sqlmodel import Session

from src.domain import model
from src.domain.model import (
    Batch,
    OrderLine,
)
from src.adapters.repository import AbstractRepository


class InvalidSku(Exception):
    pass


def allocate(order_line: OrderLine, repo: AbstractRepository, session: Session) -> str:
    batches = repo.list()

    if not is_valid_sku(order_line.sku, batches):
        raise InvalidSku(f"Invalid SKU: {order_line.sku}")

    batch_ref = model.allocate(order_line, batches)
    session.commit()

    return batch_ref


def is_valid_sku(sku: str, batches: List[Batch]):
    return sku in {batch.sku for batch in batches}
