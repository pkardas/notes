class Duck:
    def quack(self) -> None:
        raise NotImplementedError

    def fly(self) -> None:
        raise NotImplementedError


class Turkey:
    def gobble(self) -> None:
        raise NotImplementedError

    def fly(self) -> None:
        raise NotImplementedError


class WildTurkey(Turkey):
    def gobble(self) -> None:
        print("Gobble Gobble")

    def fly(self) -> None:
        print("I am flying a short distance")


class TurkeyAdapter(Duck):
    def __init__(self, turkey: Turkey):
        self._turkey = turkey

    def quack(self) -> None:
        self._turkey.gobble()

    def fly(self) -> None:
        self._turkey.fly()


# We ran out of ducks, so we use turkeys:
turkey = WildTurkey()
turkey_adapter = TurkeyAdapter(turkey)

turkey_adapter.quack()
