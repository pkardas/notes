from src import Card


def test_empty(cards_db):
    assert cards_db.count() == 0


def test_two(cards_db):
    cards_db.add_card(Card("first"))
    cards_db.add_card(Card("second"))
    assert cards_db.count() == 2


def test_three(cards_db):
    cards_db.add_card(Card("first"))
    cards_db.add_card(Card("second"))
    cards_db.add_card(Card("three"))
    assert cards_db.count() == 3
