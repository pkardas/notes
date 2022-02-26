from pydantic import BaseModel


class Event(BaseModel):
    pass


class OutOfStock(Event):
    sku: str
