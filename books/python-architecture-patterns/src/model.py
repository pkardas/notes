from dataclasses import dataclass
from datetime import date
from typing import (
    List,
    Optional,
)


@dataclass(frozen=True)
class OrderLine:
    order_id: str
    sku: str
    quantity: int


class OutOfStock(Exception):
    pass


class Batch:
    def __init__(self, ref: str, sku: str, quantity: int, eta: Optional[date]):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = quantity
        self._allocations = set()

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
        self._allocations.add(order_line)

    def deallocate(self, order_line: OrderLine) -> None:
        if order_line not in self._allocations:
            return
        self._allocations.remove(order_line)

    @property
    def allocated_quantity(self) -> int:
        return sum(line.quantity for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, order_line: OrderLine) -> bool:
        return self.sku == order_line.sku and self.available_quantity >= order_line.quantity


def allocate(line: OrderLine, batches: List[Batch]) -> str:
    try:
        batch = next(b for b in sorted(batches) if b.can_allocate(line))
    except StopIteration:
        raise OutOfStock(f"Out of stock for SKU: {line.sku}")
    batch.allocate(line)
    return batch.reference
