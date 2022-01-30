from datetime import date

from src.model import (
    Batch,
    OrderLine,
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
