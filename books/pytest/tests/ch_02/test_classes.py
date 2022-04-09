from src import Card


class TestEquality:
    def test_equality(self):
        assert Card("something", "brian", "todo", 123) == Card("something", "brian", "todo", 123)

    def test_equality_with_different_ids(self):
        assert Card("something", "brian", "todo", 123) == Card("something", "brian", "todo", 321)

    def test_inequality(self):
        assert Card("something", "brian", "todo", 123) != Card("completely different", "okken", "todo", 123)
