import pytest
from src import CardsDB


def test_no_path_raises():
    with pytest.raises(TypeError):
        CardsDB()


def test_raises_with_info():
    with pytest.raises(TypeError, match="missing 1 .* positional argument"):
        CardsDB()
