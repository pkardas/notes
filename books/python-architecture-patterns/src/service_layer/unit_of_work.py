from __future__ import annotations
from abc import (
    ABC,
    abstractmethod,
)

from sqlmodel import (
    Session,
    create_engine,
)

from src.adapters.repository import (
    AbstractRepository,
    Repository,
)
from src.config import get_postgres_uri


class AbstractUnitOfWork(ABC):
    products: AbstractRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


def default_session():
    return Session(create_engine(get_postgres_uri()))


class UnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session = default_session()):
        self.session = session

    def __enter__(self):
        self.products = Repository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
