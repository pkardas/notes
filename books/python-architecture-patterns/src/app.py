from fastapi import (
    FastAPI,
    Response,
    status,
)
from sqlalchemy import create_engine

from src import (
    config,
    views,
)
from src.adapters.orm import create_db_and_tables
from src.domain import commands
from src.domain.model import (
    Batch,
    OrderLine,
    OutOfStock,
)
from src.service_layer import message_bus
from src.service_layer.handlers import InvalidSku
from src.service_layer.unit_of_work import UnitOfWork

engine = create_engine(config.get_postgres_uri())
create_db_and_tables(engine)

api = FastAPI()


@api.post("/allocate")
async def allocate_endpoint(order_line: OrderLine, response: Response):
    try:
        message_bus.handle(
            message=commands.Allocate(order_id=order_line.order_id, sku=order_line.sku, qty=order_line.qty),
            uow=UnitOfWork()
        )
    except (OutOfStock, InvalidSku) as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": str(e)}

    return {"message": "ok"}


@api.post("/add_batch")
async def add_batch_endpoint(batch: Batch):
    message_bus.handle(
        message=commands.CreateBatch(ref=batch.reference, sku=batch.sku, qty=batch.purchased_quantity, eta=batch.eta),
        uow=UnitOfWork()
    )
    return {"message": "ok"}


@api.post("/allocate/{order_id}")
async def allocate_view_endpoint(order_id: str, response: Response):
    uow = UnitOfWork()
    if result := views.allocations(order_id, uow):
        return result
    response.status_code = status.HTTP_400_BAD_REQUEST
    return response
