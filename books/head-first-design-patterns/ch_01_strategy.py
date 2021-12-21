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
