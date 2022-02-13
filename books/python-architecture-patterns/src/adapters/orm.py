from sqlmodel import SQLModel


def create_db_and_tables(engine):
    SQLModel.metadata.create_all(engine)
