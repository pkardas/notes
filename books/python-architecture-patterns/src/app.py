from fastapi import (
    FastAPI,
    Response,
    status,
)
from sqlalchemy import create_engine
from sqlmodel import Session

from src import config

from src.domain.model import (
    OrderLine,
    OutOfStock,
)
from src.adapters.orm import create_db_and_tables
from src.adapters.repository import Repository
from src.service_layer.services import (
    InvalidSku,
    allocate,
)

engine = create_engine(config.get_postgres_uri())
create_db_and_tables(engine)

api = FastAPI()


@api.post("/allocate")
async def allocate_endpoint(order_line: OrderLine, response: Response):
    with Session(engine) as session:
        repo = Repository(session)
        try:
            batch_ref = allocate(order_line, repo, session)
        except (OutOfStock, InvalidSku) as e:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message": str(e)}

        session.commit()

    return {"batch_ref": batch_ref}
