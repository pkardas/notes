"""
API for the cards project
"""
from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field

from src.db import DB

__all__ = [
    "Card",
    "CardsDB",
    "CardsException",
    "MissingSummary",
    "InvalidCardId",
]

__version__ = "1.0.0"


@dataclass
class Card:
    summary: str = None
    owner: str = None
    state: str = "todo"
    id: int = field(default=None, compare=False)

    @classmethod
    def from_dict(cls, d):
        return Card(**d)

    def to_dict(self):
        return asdict(self)


class CardsException(Exception):
    pass


class MissingSummary(CardsException):
    pass


class InvalidCardId(CardsException):
    pass


class CardsDB:
    def __init__(self, db_path):
        self._db_path = db_path
        self._db = DB(db_path, ".cards_db")

    def add_card(self, card: Card) -> int:
        """Add a card, return the id of card."""
        if not card.summary:
            raise MissingSummary
        if card.owner is None:
            card.owner = ""
        id = self._db.create(card.to_dict())
        self._db.update(id, {"id": id})
        return id

    def get_card(self, card_id: int) -> Card:
        """Return a card with a matching id."""
        db_item = self._db.read(card_id)
        if db_item is not None:
            return Card.from_dict(db_item)
        else:
            raise InvalidCardId(card_id)

    def list_cards(self, owner=None, state=None):
        """Return a list of cards."""
        all = self._db.read_all()
        if (owner is not None) and (state is not None):
            return [
                Card.from_dict(t)
                for t in all
                if (t["owner"] == owner and t["state"] == state)
            ]
        elif owner is not None:
            return [
                Card.from_dict(t) for t in all if t["owner"] == owner
            ]
        elif state is not None:
            return [
                Card.from_dict(t) for t in all if t["state"] == state
            ]
        else:
            return [Card.from_dict(t) for t in all]
z
    def count(self) -> int:
        """Return the number of cards in db."""
        return self._db.count()

    def update_card(self, card_id: int, card_mods: Card) -> None:
        """Update a card with modifications."""
        try:
            self._db.update(card_id, card_mods.to_dict())
        except KeyError as exc:
            raise InvalidCardId(card_id) from exc

    def start(self, card_id: int):
        """Set a card state to 'in prog'."""
        self.update_card(card_id, Card(state="in prog"))

    def finish(self, card_id: int):
        """Set a card state to 'done'."""
        self.update_card(card_id, Card(state="done"))

    def delete_card(self, card_id: int) -> None:
        """Remove a card from db with given card_id."""
        try:
            self._db.delete(card_id)
        except KeyError as exc:
            raise InvalidCardId(card_id) from exc

    def delete_all(self) -> None:
        """Remove all cards from db."""
        self._db.delete_all()

    def close(self):
        self._db.close()

    def path(self):
        return self._db_path
