class CaffeineBeverage:
    def prepare_recipe(self) -> None:
        self._boil_water()
        self._brew()
        self._pour_in_cup()
        self._add_condiments()

    def _boil_water(self) -> None:
        print("Boiling water")

    def _pour_in_cup(self) -> None:
        print("Pouring in a cup")

    def _brew(self) -> None:
        raise NotImplementedError

    def _add_condiments(self) -> None:
        raise NotImplementedError


class Tea(CaffeineBeverage):
    def _brew(self) -> None:
        print("Steeping the tea")

    def _add_condiments(self) -> None:
        print("Adding Lemon")


class Coffee(CaffeineBeverage):
    def _brew(self) -> None:
        print("Dripping Coffee through filter")

    def _add_condiments(self) -> None:
        print("Adding Sugar and Milk")


Coffee().prepare_recipe()
Tea().prepare_recipe()
