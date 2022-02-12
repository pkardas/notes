from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlmodel import Session

from src import (
    config,
    model,
    repository,
)
from src.model import OrderLine
from src.orm import create_db_and_tables

engine = create_engine(config.get_postgres_uri())
create_db_and_tables(engine)

api = FastAPI()


@api.post("/allocate")
async def allocate(order_line: OrderLine):
    with Session(engine) as session:
        batches = repository.Repository(session).list()
    batch_ref = model.allocate(order_line, batches)

    return {"batch_ref": batch_ref}
