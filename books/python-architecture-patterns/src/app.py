from fastapi import (
    FastAPI,
    Response,
    status,
)

from src import views
from src.bootstrap import bootstrap
from src.domain import commands
from src.domain.model import (
    Batch,
    OrderLine,
    OutOfStock,
)
from src.service_layer.handlers import InvalidSku

bus = bootstrap()
api = FastAPI()


@api.post("/allocate")
async def allocate_endpoint(order_line: OrderLine, response: Response):
    try:
        bus.handle(commands.Allocate(order_id=order_line.order_id, sku=order_line.sku, qty=order_line.qty))
    except (OutOfStock, InvalidSku) as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": str(e)}

    return {"message": "ok"}


@api.post("/add_batch")
async def add_batch_endpoint(batch: Batch):
    bus.handle(commands.CreateBatch(ref=batch.reference, sku=batch.sku, qty=batch.purchased_quantity, eta=batch.eta))
    return {"message": "ok"}


@api.post("/allocate/{order_id}")
async def allocate_view_endpoint(order_id: str, response: Response):
    if result := views.allocations(order_id, bus.uow):
        return result
    response.status_code = status.HTTP_400_BAD_REQUEST
    return response
