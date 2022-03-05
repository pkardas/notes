import json

from src.domain.model import (
    Batch,
    OrderLine,
)


def post_to_allocate(client, order_id, sku, qty):
    return client.post("/allocate", json=json.loads(OrderLine(order_id=order_id, sku=sku, qty=qty).json()))


def get_allocation(client, order_id):
    return client.post(f"/allocate/{order_id}")


def post_to_add_batch(client, ref, sku, qty, eta):
    return client.post("/add_batch", json=json.loads(Batch(reference=ref, sku=sku, purchased_quantity=qty, eta=eta).json()))
