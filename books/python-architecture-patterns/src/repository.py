import abc

from sqlalchemy.orm import selectinload
from sqlmodel import select

from src.model import Batch


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, batch: Batch):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> Batch:
        raise NotImplementedError


class Repository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, batch):
        self.session.add(batch)
        self.session.commit()

    def get(self, reference):
        return self.session.exec(select(Batch).where(Batch.reference == reference)).one()

    def list(self):
        return self.session.exec(select(Batch).options(selectinload(Batch.allocations))).all()
