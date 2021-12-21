class Ingredient:
    def __init__(self):
        print(self.__class__.__name__)


class ThinCrustDough(Ingredient):
    pass


class ThickCrustDough(Ingredient):
    pass


class MarinaraSauce(Ingredient):
    pass


class PlumTomatoSauce(Ingredient):
    pass


class MozzarellaCheese(Ingredient):
    pass


class ReggianoCheese(Ingredient):
    pass


class Garlic(Ingredient):
    pass


class Onion(Ingredient):
    pass


class Mushroom(Ingredient):
    pass


class SlicedPepperoni(Ingredient):
    pass


class FreshClams(Ingredient):
    pass


class FrozenClams(Ingredient):
    pass


class PizzaIngredientFactory:
    def create_dough(self):
        raise NotImplementedError

    def create_sauce(self):
        raise NotImplementedError

    def create_cheese(self):
        raise NotImplementedError

    def create_veggies(self):
        raise NotImplementedError

    def create_pepperoni(self):
        raise NotImplementedError

    def create_clam(self):
        raise NotImplementedError


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_cheese(self):
        return ReggianoCheese()

    def create_veggies(self):
        return [Garlic(), Onion()]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()

    def create_cheese(self):
        return MozzarellaCheese()

    def create_veggies(self):
        return [Garlic(), Mushroom()]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FrozenClams()


class Pizza:
    name = ...

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self._ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        raise NotImplementedError

    def bake(self) -> None:
        print("Bake for 25 minutes at 350")

    def cut(self) -> None:
        print("Cutting the pizza into diagonal slices")

    def box(self) -> None:
        print("Place the pizza in official PizzaStore box")


class CheesePizza(Pizza):
    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self._ingredient_factory.create_dough()
        self._ingredient_factory.create_sauce()
        self._ingredient_factory.create_cheese()


class ClamPizza(Pizza):
    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self._ingredient_factory.create_dough()
        self._ingredient_factory.create_sauce()
        self._ingredient_factory.create_cheese()
        self._ingredient_factory.create_clam()


class PizzaStore:
    def order_pizza(self, pizza_type: str) -> Pizza:
        pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    # Factory Method:
    def create_pizza(self, pizza_type: str) -> Pizza:
        raise NotImplementedError


class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Pizza:
        ingredient_factory = NYPizzaIngredientFactory()

        match pizza_type:
            case "cheese":
                pizza = CheesePizza(ingredient_factory)
                pizza.name = "NY Style Sauce and Cheese Pizza"
            case "clam":
                pizza = ClamPizza(ingredient_factory)
                pizza.name = "NY Style Sauce and Clam Pizza"
            case _:
                raise RuntimeError("Unknown pizza type")

        return pizza


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Pizza:
        ingredient_factory = ChicagoPizzaIngredientFactory()

        match pizza_type:
            case "cheese":
                pizza = CheesePizza(ingredient_factory)
                pizza.name = "Chicago Style Deep Dish Cheese Pizza"
            case "clam":
                pizza = ClamPizza(ingredient_factory)
                pizza.name = "Chicago Style Deep Dish Clam Pizza"
            case _:
                raise RuntimeError("Unknown pizza type")

        return pizza


ny_store = NYPizzaStore()
ny_store.order_pizza("cheese")

chicago_store = ChicagoPizzaStore()
chicago_store.order_pizza("cheese")
