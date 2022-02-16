from datetime import date

import pytest

from src.domain.model import (
    Batch,
    OrderLine,
    OutOfStock,
    allocate,
)


def test_prefers_current_stock_batches_to_shipments():
    in_stock_batch = Batch(reference="in-stock-batch", sku="RETRO-CLOCK", purchased_quantity=100, eta=None)
    shipment_batch = Batch(reference="shipment-batch", sku="RETRO-CLOCK", purchased_quantity=100, eta=None)
    line = OrderLine(order_id="oref", sku="RETRO-CLOCK", quantity=10)

    allocate(line, [in_stock_batch, shipment_batch])

    assert in_stock_batch.available_quantity == 90
    assert shipment_batch.available_quantity == 100


def test_prefers_earlier_batches():
    earliest = Batch(reference="speedy-batch", sku="MINIMALIST-SPOON", purchased_quantity=100, eta=date(2022, 1, 7))
    medium = Batch(reference="normal-batch", sku="MINIMALIST-SPOON", purchased_quantity=100, eta=date(2022, 1, 8))
    latest = Batch(reference="slow-batch", sku="MINIMALIST-SPOON", purchased_quantity=100, eta=date(2022, 1, 9))
    line = OrderLine(order_id="oref", sku="MINIMALIST-SPOON", quantity=10)

    allocate(line, [earliest, medium, latest])

    assert earliest.available_quantity == 90
    assert medium.available_quantity == 100
    assert latest.available_quantity == 100


def test_returns_allocated_batch_ref():
    in_stock_batch = Batch(reference="in-stock-batch-ref", sku="HIGHBROW-POSTER", purchased_quantity=100, eta=None)
    shipment_batch = Batch(reference="shipment-batch-ref", sku="HIGHBROW-POSTER", purchased_quantity=100, eta=date(2022, 1, 7))
    line = OrderLine(order_id="oref", sku="HIGHBROW-POSTER", quantity=10)

    allocation = allocate(line, [in_stock_batch, shipment_batch])

    assert allocation == in_stock_batch.reference


def test_raises_out_of_stock_exceptions_if_cannot_allocate():
    batch = Batch(reference="batch", sku="SMALL-FORM", purchased_quantity=10, eta=date(2022, 1, 7))
    allocate(OrderLine(order_id="oref", sku="SMALL-FORM", quantity=10), [batch])

    with pytest.raises(OutOfStock, match="SMALL-FORM"):
        allocate(OrderLine(order_id="oref", sku="SMALL-FORM", quantity=1), [batch])
