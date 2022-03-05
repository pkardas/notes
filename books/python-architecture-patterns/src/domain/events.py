from pydantic import BaseModel


class Event(BaseModel):
    pass


class OutOfStock(Event):
    sku: str


class Allocated(Event):
    order_id: str
    sku: str
    qty: int
    batch_ref: str


class Deallocated(Event):
    order_id: str
    sku: str
    qty: int


class BatchQuantityChanged(Event):
    batch_ref: str
    qty: int
