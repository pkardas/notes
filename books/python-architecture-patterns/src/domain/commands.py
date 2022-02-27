from dataclasses import dataclass
from datetime import date
from typing import Optional


class Command:
    pass


@dataclass
class Allocate(Command):
    order_id: str
    sku: str
    qty: int


@dataclass
class CreateBatch(Command):
    ref: str
    sku: str
    qty: int
    eta: Optional[date] = None


@dataclass
class ChangeBatchQuantity(Command):
    ref: str
    qty: int
