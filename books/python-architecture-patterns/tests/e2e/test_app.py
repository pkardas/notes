from uuid import uuid4

from src.domain.model import OrderLine


def random_suffix():
    return uuid4().hex[:6]


def random_sku(name=''):
    return f"sku-{name}-{random_suffix()}"


def random_batch_ref(name=''):
    return f"batch-{name}-{random_suffix()}"


def random_order_id(name=''):
    return f"order-{name}-{random_suffix()}"


def test_happy_path_returns_200_and_allocated_batch(add_stock, client):
    sku, other_sku = random_sku(), random_sku("other")
    early_batch, later_batch, other_batch = random_batch_ref('1'), random_batch_ref('2'), random_batch_ref('3')
    add_stock([
        (later_batch, sku, 100, "2011-01-02"),
        (early_batch, sku, 100, "2011-01-01"),
        (other_batch, other_sku, 100, None),
    ])

    response = client.post("/allocate", json=OrderLine(order_id=random_order_id(), sku=sku, quantity=3).dict())

    assert response.status_code == 200, response.status_code
    assert response.json()["batch_ref"] == early_batch


def test_unhappy_path_returns_400_and_error_message(client):
    unknown_sku = random_sku()
    response = client.post("/allocate", json=OrderLine(order_id=random_order_id(), sku=unknown_sku, quantity=20).dict())

    assert response.status_code == 400
    assert response.json()["message"] == f"Invalid SKU: {unknown_sku}"
