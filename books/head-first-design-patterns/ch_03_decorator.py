class Beverage:
    @property
    def description(self) -> str:
        return self.__class__.__name__

    @property
    def cost(self) -> float:
        raise NotImplementedError


class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    @property
    def description(self) -> str:
        return f"{self._beverage.description}, {super(CondimentDecorator, self).description}"

    @property
    def cost(self) -> float:
        raise NotImplementedError


class Espresso(Beverage):
    @property
    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    @property
    def cost(self) -> float:
        return 0.89


class Mocha(CondimentDecorator):
    @property
    def cost(self) -> float:
        return self._beverage.cost + 0.20


class Soy(CondimentDecorator):
    @property
    def cost(self) -> float:
        return self._beverage.cost + 0.15


beverage = Espresso()
beverage = Mocha(beverage)
beverage = Mocha(beverage)
beverage = Soy(beverage)
print(f"${beverage.cost} for '{beverage.description}'")
