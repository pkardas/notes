from datetime import date
from uuid import uuid4

from tests.e2e.api_client import (
    get_allocation,
    post_to_add_batch,
    post_to_allocate,
)


def random_suffix():
    return uuid4().hex[:6]


def random_sku(name=''):
    return f"sku-{name}-{random_suffix()}"


def random_batch_ref(name=''):
    return f"batch-{name}-{random_suffix()}"


def random_order_id(name=''):
    return f"order-{name}-{random_suffix()}"


def test_happy_path_returns_200_and_allocated_batch(client):
    sku, other_sku = random_sku(), random_sku("other")
    order_id = random_order_id()
    early_batch, later_batch, other_batch = random_batch_ref('1'), random_batch_ref('2'), random_batch_ref('3')
    post_to_add_batch(client, later_batch, sku, 100, date(2011, 1, 2))
    post_to_add_batch(client, early_batch, sku, 100, date(2011, 1, 1))
    post_to_add_batch(client, other_batch, other_sku, 100, None)

    response = post_to_allocate(client=client, order_id=order_id, sku=sku, qty=3)
    assert response.status_code == 200, response.status_code

    response = get_allocation(client=client, order_id=order_id)
    assert response.status_code == 200
    assert response.json() == [{"sku": sku, "batch_ref": early_batch}]


def test_unhappy_path_returns_400_and_error_message(client):
    unknown_order_id, unknown_sku = random_order_id(), random_sku()
    response = post_to_allocate(client=client, order_id=random_order_id(), sku=unknown_sku, qty=20)

    assert response.status_code == 400
    assert response.json()["message"] == f"Invalid SKU: {unknown_sku}"

    response = get_allocation(client=client, order_id=unknown_order_id)
    assert response.status_code == 400
