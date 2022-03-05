from sqlmodel import (
    Field,
    SQLModel,
)


class AllocationsView(SQLModel, table=True):
    id: int = Field(primary_key=True)
    order_id: str
    sku: str
    batch_ref: str


def create_db_and_tables(engine):
    SQLModel.metadata.create_all(engine)


def clean_db_and_tables(engine):
    SQLModel.metadata.drop_all(engine)
