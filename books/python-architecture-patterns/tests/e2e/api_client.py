import json

from src.domain.model import (
    Batch,
    OrderLine,
)


def post_to_allocate(client, order_id, sku, qty):
    response = client.post("/allocate", json=json.loads(OrderLine(order_id=order_id, sku=sku, qty=qty).json()))
    assert response.status_code == 200
    return response


def post_to_add_batch(client, ref, sku, qty, eta):
    response = client.post("/add_batch", json=json.loads(Batch(reference=ref, sku=sku, purchased_quantity=qty, eta=eta).json()))
    assert response.status_code == 200
