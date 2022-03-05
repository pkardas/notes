from typing import (
    Dict,
    List,
)

from src.service_layer.unit_of_work import UnitOfWork


def allocations(order_id: str, uow: UnitOfWork) -> List[Dict]:
    with uow:
        results = uow.session.execute(
            "SELECT sku, batch_ref FROM allocationsview WHERE order_id = :order_id",
            dict(order_id=order_id),
        )
    return [dict(r) for r in results]
