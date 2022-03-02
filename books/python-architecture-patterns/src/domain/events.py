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


class BatchQuantityChanged(BaseModel):
    batch_ref: str
    qty: int
