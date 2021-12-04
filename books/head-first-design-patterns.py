# Chapter 1 - The Strategy Pattern

class FlyBehavior:
    def fly(self) -> None:
        raise NotImplementedError


class QuackBehavior:
    def quack(self) -> None:
        raise NotImplementedError


class Duck:
    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior) -> None:
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def perform_fly(self) -> None:
        self.fly_behavior.fly()

    def perform_quack(self) -> None:
        self.quack_behavior.quack()

    def display(self) -> None:
        raise NotImplementedError


class FlyWithWings(FlyBehavior):
    def fly(self) -> None:
        print("I am using wings!")


class FlyNoWay(FlyBehavior):
    def fly(self) -> None:
        print("I am not flying.")


class Quack(QuackBehavior):
    def quack(self) -> None:
        print("QUACK")


class Squeak(QuackBehavior):
    def quack(self) -> None:
        print("SQUEAK")


class MuteQuack(QuackBehavior):
    def quack(self) -> None:
        print("<SILENCE>")


class MallardDuck(Duck):
    def __init__(self) -> None:
        super().__init__(FlyWithWings(), Quack())

    def display(self) -> None:
        print("Looks like a mallard.")


duck = MallardDuck()
duck.display()
duck.perform_fly()
duck.perform_quack()


# Chapter 2 - The Observer Pattern

class Observer:
    def update(self) -> None:
        raise NotImplementedError


class Subject:
    def register_observer(self, observer: Observer) -> None:
        raise NotImplementedError

    def remove_observer(self, observer: Observer) -> None:
        raise NotImplementedError

    def notify_observers(self) -> None:
        raise NotImplementedError


class DisplayElement:
    def display(self) -> None:
        raise NotImplementedError


class WeatherData(Subject):
    def __init__(self):
        self._observers = []
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()

    def set_measurements(self, temperature: float, humidity: float, pressure: float) -> None:
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        self._temperature = 0.0
        self._humidity = 0.0
        self._weather_data = weather_data
        self._weather_data.register_observer(self)

    def display(self) -> None:
        print(f"Current conditions: {self._temperature}°C, {self._humidity}%")

    def update(self) -> None:
        self._temperature = self._weather_data.temperature
        self._humidity = self._weather_data.humidity
        self.display()


class AvgTempDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        self._temperature = []
        self._weather_data = weather_data
        self._weather_data.register_observer(self)

    def display(self) -> None:
        print(f"Average temperature: {sum(self._temperature) / len(self._temperature)}°C")

    def update(self) -> None:
        self._temperature.append(self._weather_data.temperature)
        self.display()


weather_data = WeatherData()
current_display = CurrentConditionsDisplay(weather_data)
forecast_display = AvgTempDisplay(weather_data)

weather_data.set_measurements(23.0, 68.1, 1018.0)
weather_data.set_measurements(24.2, 70.4, 1019.2)
weather_data.set_measurements(25.8, 71.2, 1018.4)


# Chapter 3 - The Decorator Pattern

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


# Chapter 4 - The Factory Method and Abstract Factory Patterns

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


# Abstract Factory:
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


# Chapter 5 - The Singleton Pattern
# Implementation using '__new__':
class ChocolateBoiler:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ChocolateBoiler, cls).__new__(cls)
        return cls._instance


boiler_0 = ChocolateBoiler()
boiler_1 = ChocolateBoiler()

print(f"#0: {boiler_0}")
print(f"#1: {boiler_1}")
print(f"Are they the same object? {boiler_0 is boiler_1}")


# Implementation using variable - instantiated on module import:
class ChocolateBoiler:
    pass


chocolate_boiler = ChocolateBoiler()
print(f"Are they the same object? {chocolate_boiler is chocolate_boiler}")


# Implementation using function - using 'attr':
def get_chocolate_boiler() -> ChocolateBoiler:
    if not hasattr(get_chocolate_boiler, "instance"):
        setattr(get_chocolate_boiler, "instance", ChocolateBoiler())
    return getattr(get_chocolate_boiler, "instance")


print(f"Are they the same object? {get_chocolate_boiler() is get_chocolate_boiler()}")

# Implementation using function - using variable:
_chocolate_boiler = None


def get_chocolate_boiler() -> ChocolateBoiler:
    global _chocolate_boiler

    if not _chocolate_boiler:
        _chocolate_boiler = ChocolateBoiler()

    return _chocolate_boiler


print(f"Are they the same object? {get_chocolate_boiler() is get_chocolate_boiler()}")

# Chapter 6 - The Command Pattern
from typing import List


class Device:
    @property
    def name(self) -> str:
        return self.__class__.__name__

    def on(self) -> None:
        print(f"{self.name} was turned on")

    def off(self) -> None:
        print(f"{self.name} was turned off")


class Light(Device):
    pass


class Tv(Device):
    pass


class Stereo(Device):
    def __init__(self) -> None:
        self.volume = 0

    def set_cd(self) -> None:
        print(f"{self.name} CD set")

    def set_volume(self, volume: int) -> None:
        print(f"{self.name} Volume set to {volume}")
        self.volume = volume


class Command:
    def execute(self) -> None:
        raise NotImplementedError

    def undo(self) -> None:
        raise NotImplementedError


class NoCommand(Command):
    def execute(self) -> None:
        pass

    def undo(self) -> None:
        pass


class MarcoCommand(Command):
    def __init__(self, commands: List[Command]):
        self._commands = commands

    def execute(self) -> None:
        for command in self._commands:
            command.execute()

    def undo(self) -> None:
        for command in self._commands[::-1]:
            command.undo()


class DeviceOnCommand(Command):
    def __init__(self, device: Device) -> None:
        self._device = device

    def execute(self) -> None:
        self._device.on()

    def undo(self) -> None:
        self._device.off()


class DeviceOffCommand(Command):
    def __init__(self, device: Device) -> None:
        self._device = device

    def execute(self) -> None:
        self._device.off()

    def undo(self) -> None:
        self._device.on()


class StereoVolumeUpCommand(Command):
    def __init__(self, stereo: Stereo) -> None:
        self._stereo = stereo

    def execute(self) -> None:
        self._stereo.set_volume(stereo.volume + 1)

    def undo(self) -> None:
        self._stereo.set_volume(stereo.volume - 1)


class RemoteControl:
    def __init__(self):
        self._on_commands = [NoCommand()] * 7
        self._off_commands = [NoCommand()] * 7
        self._undo_commands = []

    def set_command(self, slot: int, on_command: Command, off_command: Command) -> None:
        self._on_commands[slot] = on_command
        self._off_commands[slot] = off_command

    def on_button_pushed(self, slot: int) -> None:
        self._on_commands[slot].execute()
        self._undo_commands.append(self._on_commands[slot])

    def off_button_pushed(self, slot: int) -> None:
        self._off_commands[slot].execute()
        self._undo_commands.append(self._off_commands[slot])

    def undo_button_pushed(self) -> None:
        if not self._undo_commands:
            return
        self._undo_commands.pop().undo()


light = Light()
tv = Tv()
stereo = Stereo()

light_on_command, light_off_command = DeviceOnCommand(light), DeviceOffCommand(light)
tv_on_command, tv_off_command = DeviceOnCommand(tv), DeviceOffCommand(tv)
stereo_on_command, stereo_off_command = DeviceOnCommand(stereo), DeviceOffCommand(stereo)

volume_up_command = StereoVolumeUpCommand(stereo)

party_on_command = MarcoCommand([light_on_command, tv_on_command, stereo_on_command, volume_up_command])
party_off_command = MarcoCommand([light_on_command, tv_on_command, stereo_off_command])

remote = RemoteControl()
remote.set_command(0, light_on_command, light_off_command)
remote.set_command(1, tv_on_command, tv_off_command)
remote.set_command(2, stereo_on_command, stereo_off_command)
remote.set_command(3, party_on_command, party_off_command)

remote.on_button_pushed(1)
remote.on_button_pushed(3)
remote.undo_button_pushed()
