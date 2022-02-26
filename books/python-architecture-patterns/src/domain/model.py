from datetime import date
from typing import (
    Iterable,
    List,
    Optional,
    cast,
)

from pydantic import PrivateAttr
from pydantic.fields import ModelPrivateAttr
from sqlmodel import (
    Field,
    Relationship,
    SQLModel,
)

from src.domain import events
from src.domain.events import Event


class OutOfStock(Exception):
    pass


class OrderLine(SQLModel, table=True):
    order_id: str
    sku: str
    quantity: int
    # DB-specific fields:
    id: Optional[int] = Field(default=None, primary_key=True)
    batch_id: Optional[int] = Field(default=None, foreign_key="batch.id")
    batch: Optional["Batch"] = Relationship(back_populates="allocations")


class Batch(SQLModel, table=True):
    reference: str
    sku: str
    purchased_quantity: int
    eta: Optional[date]
    allocations: List["OrderLine"] = Relationship(back_populates="batch")
    # DB-specific fields:
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    product: Optional["Product"] = Relationship(back_populates="batches")

    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference

    def __hash__(self):
        return hash(self.reference)

    def __gt__(self, other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta

    def allocate(self, order_line: OrderLine) -> None:
        if not self.can_allocate(order_line):
            return
        if order_line in self.allocations:
            return
        self.allocations.append(order_line)

    def deallocate(self, order_line: OrderLine) -> None:
        if order_line not in self.allocations:
            return
        self.allocations.remove(order_line)

    @property
    def allocated_quantity(self) -> int:
        return sum(line.quantity for line in self.allocations)

    @property
    def available_quantity(self) -> int:
        return self.purchased_quantity - self.allocated_quantity

    def can_allocate(self, order_line: OrderLine) -> bool:
        return self.sku == order_line.sku and self.available_quantity >= order_line.quantity


class Product(SQLModel, table=True):
    sku: str
    batches: List["Batch"] = Relationship(back_populates="product")
    # DB-specific fields:
    id: Optional[int] = Field(default=None, primary_key=True)
    version_number: int = 0
    # DB excluded fields:
    _events: ModelPrivateAttr = PrivateAttr(default=[])

    def __hash__(self):
        return hash(self.sku)

    @property
    def events(self) -> List[Event]:
        return self._events.default

    def allocate(self, order_line: OrderLine) -> Optional[str]:
        try:
            batch = next(b for b in sorted(cast(Iterable, self.batches)) if b.can_allocate(order_line))
        except StopIteration:
            self.events.append(events.OutOfStock(sku=order_line.sku))
            return None
        batch.allocate(order_line)
        self.version_number += 1
        return batch.reference
