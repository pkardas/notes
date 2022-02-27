from typing import (
    Optional,
    Protocol,
    Set,
)

from sqlmodel import (
    Session,
    select,
)

from src.domain.model import (
    Batch,
    Product,
)


class AbstractRepository(Protocol):
    def add(self, product: Product):
        ...

    def get(self, sku: str) -> Optional[Product]:
        ...

    def get_by_batch_ref(self, ref: str) -> Optional[Product]:
        ...


class Repository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, product: Product):
        self.session.add(product)
        self.session.commit()

    def get(self, sku: str) -> Optional[Product]:
        return self.session.exec(select(Product).where(Product.sku == sku)).first()

    def get_by_batch_ref(self, ref: str) -> Optional[Product]:
        return self.session.exec(select(Product).join(Batch).where(Batch.reference == ref)).first()


class TrackingRepository(AbstractRepository):
    seen: Set[Product]

    def __init__(self, repo: AbstractRepository):
        super().__init__()
        self.seen = set()
        self._repo = repo

    def add(self, product: Product):
        self._repo.add(product)
        self.seen.add(product)

    def get(self, sku: str) -> Optional[Product]:
        product = self._repo.get(sku)
        if product:
            self.seen.add(product)
        return product

    def get_by_batch_ref(self, ref: str) -> Optional[Product]:
        if product := self._repo.get_by_batch_ref(ref):
            self.seen.add(product)
        return product
