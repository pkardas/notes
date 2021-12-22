from collections.abc import Iterator
from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Union,
)


@dataclass
class MenuItem:
    name: str
    description: str
    vegetarian: bool
    price: float


class DinnerMenuIterator(Iterator):
    # Just for demonstration purposes!
    def __init__(self, collection: List[MenuItem]):
        self._collection = collection
        self._position = 0

    def __next__(self) -> MenuItem:
        try:
            value = self._collection[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()

        return value


class DinnerMenu:
    # Just for demonstration purposes!
    menu = [
        MenuItem("Vegetarian BLT", "Fake Bacon with lettuce on whole wheat", True, 2.99),
        MenuItem("BLT", "Bacon with lettuce on whole wheat", False, 2.99),
        MenuItem("Soup of the day", "Soup of the day, with a side of potato salad", False, 3.99),
        MenuItem("HotDog", "A Hot Dog with sauerkraut, relish, onions, topped with cheese", False, 3.05),
    ]

    def __iter__(self) -> DinnerMenuIterator:
        # Factory Method
        return DinnerMenuIterator(self.menu)


class BreakfastMenuIterator(Iterator):
    # Just for demonstration purposes!
    def __init__(self, collection: Dict[str, MenuItem]):
        self._collection = collection
        self._position = 0

    def __next__(self) -> MenuItem:
        try:
            value = list(self._collection.values())[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()

        return value


class BreakfastMenu:
    # Just for demonstration purposes!
    menu = {
        "K&B's Pancake Breakfast": MenuItem("K&B's Pancake Breakfast", "Pancakes with scrambled eggs and toast", True, 2.99),
        "Regular Pancake Breakfast": MenuItem("Regular Pancake Breakfast", "Pancakes with fried eggs, sausage", False, 2.99),
        "Blueberry Pancakes": MenuItem("Blueberry Pancakes", "Pancakes made with fresh blueberries", True, 3.49),
    }

    def __iter__(self) -> BreakfastMenuIterator:
        # Factory Method
        return BreakfastMenuIterator(self.menu)


class Waitress:
    def __init__(self, pancake_menu: BreakfastMenu, dinner_menu: DinnerMenu):
        self._pancake_menu = pancake_menu
        self._dinner_menu = dinner_menu

    def print_menu(self):
        print("BREAKFAST")
        self._print_menu(self._pancake_menu)
        print("DINNER")
        self._print_menu(self._dinner_menu)

    @staticmethod
    def _print_menu(menu: Union[BreakfastMenu, DinnerMenu]):
        for menu_item in menu:
            print(f"{menu_item.name}, {menu_item.price}, {menu_item.description}")


Waitress(BreakfastMenu(), DinnerMenu()).print_menu()
