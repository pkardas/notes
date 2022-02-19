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
    batches: AbstractRepository

    def __enter__(self):
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
    engine = create_engine(get_postgres_uri())
    return Session(engine)


class UnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session = default_session()):
        self.session = session

    def __enter__(self):
        self.batches = Repository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
