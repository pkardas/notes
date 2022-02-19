from abc import (
    ABC,
    abstractmethod,
)
from typing import List

from sqlalchemy.orm import selectinload
from sqlmodel import (
    Session,
    select,
)

from src.domain.model import Batch


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, batch: Batch):
        raise NotImplementedError

    @abstractmethod
    def get(self, reference) -> Batch:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[Batch]:
        raise NotImplementedError


class Repository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, batch):
        self.session.add(batch)
        self.session.commit()

    def get(self, reference):
        return self.session.exec(select(Batch).where(Batch.reference == reference)).one()

    def list(self):
        return self.session.exec(select(Batch).options(selectinload(Batch.allocations))).all()
