from datetime import date
from typing import (
    List,
    Optional,
)

from sqlmodel import (
    Field,
    Relationship,
    SQLModel,
)


# TODO: Separate DB fields from business fields using inheritance or making them "private"

class OutOfStock(Exception):
    pass


class OrderLine(SQLModel, table=True):
    order_id: str
    sku: str
    quantity: int
    # DB fields:
    id: Optional[int] = Field(default=None, primary_key=True)
    batch_id: Optional[int] = Field(default=None, foreign_key="batch.id")
    batch: Optional["Batch"] = Relationship(back_populates="allocations")


class Batch(SQLModel, table=True):
    reference: str
    sku: str
    purchased_quantity: int
    eta: Optional[date]
    allocations: List["OrderLine"] = Relationship(back_populates="batch")
    # DB fields:
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
    # DB fields:
    id: Optional[int] = Field(default=None, primary_key=True)

    def __hash__(self):
        return hash(self.sku)

    def allocate(self, order_line: OrderLine):
        try:
            batch = next(b for b in sorted(self.batches) if b.can_allocate(order_line))
        except StopIteration:
            raise OutOfStock(f"Out of stock for SKU: {order_line.sku}")
        batch.allocate(order_line)
        return batch.reference
