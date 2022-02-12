from uuid import uuid4

import pytest

from src.model import OrderLine


def random_suffix():
    return uuid4().hex[:6]


def random_sku(name=''):
    return f"sku-{name}-{random_suffix()}"


def random_batch_ref(name=''):
    return f"batch-{name}-{random_suffix()}"


def random_order_id(name=''):
    return f"order-{name}-{random_suffix()}"


@pytest.mark.usefixtures("restart_api")
def test_api_returns_allocation(add_stock, client):
    sku, order_sku = random_sku(), random_sku("other")
    early_batch, later_batch, other_batch = random_batch_ref('1'), random_batch_ref('2'), random_batch_ref('3')
    add_stock([
        (later_batch, sku, 100, "2011-01-02"),
        (early_batch, sku, 100, "2011-01-01"),
        (other_batch, order_sku, 100, None),
    ])

    response = client.post("/allocate", json=OrderLine(order_id=random_order_id(), sku=sku, quantity=3).dict())

    assert response.status_code == 200, response.status_code
    assert response.json()["batch_ref"] == early_batch
