from __future__ import annotations

from abc import ABC
from dataclasses import dataclass


class MenuComponent:
    def add(self, menu_component: MenuComponent):
        raise NotImplementedError

    def remove(self, menu_component: MenuComponent):
        raise NotImplementedError

    def get_child(self, i: int):
        raise NotImplementedError

    def print(self):
        raise NotImplementedError


@dataclass
class MenuItem(MenuComponent, ABC):
    name: str
    description: str
    vegetarian: bool
    price: float

    def print(self):
        print(f"{self.name}, {self.price}, {self.description}")


class Menu(MenuComponent):
    def __init__(self, name: str):
        self._name = name
        self._menu_components = []

    def add(self, menu_component: MenuComponent):
        self._menu_components.append(menu_component)

    def remove(self, menu_component: MenuComponent):
        self._menu_components.remove(menu_component)

    def get_child(self, i: int):
        return self._menu_components[i]

    def print(self):
        print(self._name)
        for menu_component in self._menu_components:
            menu_component.print()


class Waitress:
    def __init__(self, menu_component: MenuComponent):
        self._menu_component = menu_component

    def print_menu(self):
        self._menu_component.print()


breakfast_menu = Menu("BREAKFAST")
dinner_menu = Menu("DINNER")
dessert_menu = Menu("DESSERT")

all_menus = Menu("ALL MENUS")
all_menus.add(breakfast_menu)
all_menus.add(dinner_menu)

dinner_menu.add(MenuItem("Pasta", "Pasta with marinara Sauce", True, 3.89))
dinner_menu.add(dessert_menu)

dessert_menu.add(MenuItem("Apple Pie", "Apple pie with a flaky crust, topped with vanilla ice cream", True, 1.59))

Waitress(all_menus).print_menu()
