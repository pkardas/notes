from datetime import (
    date,
)

import pytest

from src.model import (
    Batch,
    OrderLine,
    OutOfStock,
    allocate,
)


def batch_and_line(sku, batch_qty, line_qty):
    return Batch("batch-001", sku, quantity=batch_qty, eta=date.today()), OrderLine("order-123", sku, line_qty)


def test_allocating_to_batch_reduces_available_quantity():
    batch, line = batch_and_line("SMALL-TABLE", 20, 2)
    batch.allocate(line)
    assert batch.available_quantity == 18


def test_can_allocate_if_available_greater_than_required():
    large_batch, small_line = batch_and_line("ELEGANT-LAMP", 20, 2)
    assert large_batch.can_allocate(small_line)


def test_cannot_allocate_if_available_smaller_than_required():
    small_batch, large_line = batch_and_line("ELEGANT-LAMP", 2, 20)
    assert not small_batch.can_allocate(large_line)


def test_not_allocate_if_available_equal_to_required():
    small_batch, large_line = batch_and_line("ELEGANT-LAMP", 2, 2)
    assert small_batch.can_allocate(large_line)


def test_cannot_allocate_if_skus_dont_match():
    batch = Batch("batch-001", "UNCOMFORTABLE-CHAIN", quantity=100, eta=None)
    different_sku_line = OrderLine("order-123", "EXPENSIVE-TOASTER", 10)
    assert not batch.can_allocate(different_sku_line)


def test_can_only_deallocate_allocated_lines():
    batch, unallocated_line = batch_and_line("DECORATIVE-TRINKET", 20, 2)
    batch.deallocate(unallocated_line)
    assert batch.available_quantity == 20


def test_allocation_is_idempotent():
    batch, line = batch_and_line("ANGULAR-DESK", 20, 2)
    batch.allocate(line)
    batch.allocate(line)
    assert batch.available_quantity == 18


def test_prefers_current_stock_batches_to_shipments():
    in_stock_batch = Batch("in-stock-batch", "RETRO-CLOCK", quantity=100, eta=None)
    shipment_batch = Batch("shipment-batch", "RETRO-CLOCK", quantity=100, eta=None)
    line = OrderLine("oref", "RETRO-CLOCK", 10)

    allocate(line, [in_stock_batch, shipment_batch])

    assert in_stock_batch.available_quantity == 90
    assert shipment_batch.available_quantity == 100


def test_prefers_earlier_batches():
    earliest = Batch("speedy-batch", "MINIMALIST-SPOON", quantity=100, eta=date(2022, 1, 7))
    medium = Batch("normal-batch", "MINIMALIST-SPOON", quantity=100, eta=date(2022, 1, 8))
    latest = Batch("slow-batch", "MINIMALIST-SPOON", quantity=100, eta=date(2022, 1, 9))
    line = OrderLine("oref", "MINIMALIST-SPOON", 10)

    allocate(line, [earliest, medium, latest])

    assert earliest.available_quantity == 90
    assert medium.available_quantity == 100
    assert latest.available_quantity == 100


def test_returns_allocated_batch_ref():
    in_stock_batch = Batch("in-stock-batch-ref", "HIGHBROW-POSTER", quantity=100, eta=None)
    shipment_batch = Batch("shipment-batch-ref", "HIGHBROW-POSTER", quantity=100, eta=date(2022, 1, 7))
    line = OrderLine("oref", "HIGHBROW-POSTER", 10)

    allocation = allocate(line, [in_stock_batch, shipment_batch])

    assert allocation == in_stock_batch.reference


def test_raises_out_of_stock_exceptions_if_cannot_allocate():
    batch = Batch("batch", "SMALL-FORM", quantity=10, eta=date(2022, 1, 7))
    allocate(OrderLine("oref", "SMALL-FORM", 10), [batch])

    with pytest.raises(OutOfStock, match="SMALL-FORM"):
        allocate(OrderLine("oref", "SMALL-FORM", 1), [batch])
