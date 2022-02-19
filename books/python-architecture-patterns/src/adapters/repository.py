from abc import (
    ABC,
    abstractmethod,
)
from typing import Optional

from sqlalchemy.exc import NoResultFound
from sqlmodel import (
    Session,
    select,
)

from src.domain.model import Product


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, product: Product):
        raise NotImplementedError

    @abstractmethod
    def get(self, sku: str) -> Optional[Product]:
        raise NotImplementedError


class Repository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, product: Product):
        self.session.add(product)
        self.session.commit()

    def get(self, sku: str) -> Optional[Product]:
        try:
            return self.session.exec(select(Product).where(Product.sku == sku)).one()
        except NoResultFound:
            return None
