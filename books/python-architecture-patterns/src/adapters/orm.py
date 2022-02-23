from sqlmodel import SQLModel


def create_db_and_tables(engine):
    SQLModel.metadata.create_all(engine)


def clean_db_and_tables(engine):
    SQLModel.metadata.drop_all(engine)
