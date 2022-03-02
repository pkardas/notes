import json
from datetime import date

import pytest
from tenacity import (
    Retrying,
    stop_after_delay,
)

from tests.e2e import redis_client
from tests.e2e.api_client import (
    post_to_add_batch,
    post_to_allocate,
)
from tests.e2e.test_app import (
    random_batch_ref,
    random_order_id,
    random_sku,
)


def test_change_batch_quantity_leading_to_allocation(client):
    order_id, sku = random_order_id(), random_sku()
    earlier_batch, later_batch = random_batch_ref("old"), random_batch_ref("new")
    post_to_add_batch(client=client, ref=earlier_batch, sku=sku, qty=10, eta=date(2021, 1, 1))
    post_to_add_batch(client=client, ref=later_batch, sku=sku, qty=10, eta=date(2021, 1, 2))

    response = post_to_allocate(client=client, order_id=order_id, sku=sku, qty=10)
    assert response.json()["batch_ref"] == earlier_batch

    subscription = redis_client.subscribe_to("line_allocated")

    redis_client.publish_message("change_batch_quantity", {"batch_ref": earlier_batch, "qty": 5})

    # it may take some for message to arrive:
    for attempt in Retrying(stop=stop_after_delay(3), reraise=True):
        with attempt:
            message = subscription.get_message(timeout=1)
            if not message:
                continue
            data = json.loads(message["data"])
            assert data["order_id"] == order_id
            assert data["batch_ref"] == later_batch
    if not message:
        pytest.fail("Message not fetched")
