from __future__ import annotations

from random import random


class State:
    def __init__(self, gumball_machine: GumballMachine):
        self._gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        pass

    def eject_quarter(self) -> None:
        pass

    def turn_crank(self) -> None:
        pass

    def dispense(self) -> None:
        pass


class NoQuarterState(State):
    def insert_quarter(self) -> None:
        print("You inserted a quarter")
        self._gumball_machine.state = self._gumball_machine.has_quarter_state


class HasQuarterState(State):
    def eject_quarter(self) -> None:
        print("Quarter returned")
        self._gumball_machine.state = self._gumball_machine.no_quarter_state

    def turn_crank(self) -> None:
        print("You turned...")

        if random() < 0.1 and self._gumball_machine.count > 1:
            self._gumball_machine.state = self._gumball_machine.winner_state
        else:
            self._gumball_machine.state = self._gumball_machine.sold_state


class SoldState(State):
    def dispense(self) -> None:
        self._gumball_machine.release_ball()

        if self._gumball_machine.count > 0:
            self._gumball_machine.state = self._gumball_machine.no_quarter_state
        else:
            print("Out of gumballs!")
            self._gumball_machine.state = self._gumball_machine.sold_out_state


class SoldOutState(State):
    pass


class WinnerState(State):
    def dispense(self) -> None:
        self._gumball_machine.release_ball()

        if self._gumball_machine.count == 0:
            self._gumball_machine.state = self._gumball_machine.sold_out_state
        else:
            self._gumball_machine.release_ball()
            print("You are a WINNER!")

            if self._gumball_machine.count > 0:
                self._gumball_machine.state = self._gumball_machine.no_quarter_state
            else:
                print("Out of gumballs!")
                self._gumball_machine.state = self._gumball_machine.sold_out_state


class GumballMachine:
    def __init__(self, count: int):
        self.count = count

        self.no_quarter_state = NoQuarterState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_state = SoldState(self)
        self.sold_out_state = SoldOutState(self)
        self.winner_state = WinnerState(self)

        self.state = self.no_quarter_state if count > 0 else self.sold_out_state

    def insert_quarter(self) -> None:
        self.state.insert_quarter()

    def eject_quarter(self) -> None:
        self.state.eject_quarter()

    def turn_crank(self) -> None:
        self.state.turn_crank()
        self.state.dispense()

    def release_ball(self) -> None:
        print("A ball rolling out the slot...")
        if self.count > 0:
            self.count = self.count - 1


machine = GumballMachine(5)

machine.insert_quarter()
machine.turn_crank()

machine.insert_quarter()
machine.turn_crank()

machine.insert_quarter()
machine.turn_crank()
