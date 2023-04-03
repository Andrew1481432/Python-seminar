import inspect
from enum import Enum


class MealyError(Exception):
    def __init__(self, message):
        super().__init__(message)


class State(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    H = 7


class StateMachine:
    state = State.A

    def jump(self):
        return self.update({
            State.A: [State.B, 0],
            State.D: [State.E, 5],
            State.E: [State.F, 6],
        })

    def bend(self):
        return self.update({
            State.A: [State.F, 1],
            State.B: [State.C, 2],
            State.C: [State.D, 4],
            State.E: [State.C, 8],
        })

    def turn(self):
        return self.update({
            State.B: [State.E, 3],
            State.E: [State.A, 7],
        })

    def update(self, transitions):
        if self.state in transitions:
            self.state, signal = transitions[self.state]
            return signal
        else:
            raise MealyError(inspect.stack()[1][3])


def main():
    return StateMachine()


def test():
    o = main()
    o.jump()  # 0
    o.turn()  # 3
    o.bend()  # 8
    o.bend()  # 4
    o.jump()  # 5
    o.turn()  # 7
    o.jump()  # 0
    o.bend()  # 2
    o.bend()  # 4
    o.jump()  # 5
    o.turn()  # 7
    o.bend()  # 1

    o1 = main()
    o1.jump()  # 0
    o1.turn()  # 3
    o1.bend()  # 8
    o1.bend()  # 4
    o1.jump()  # 5
    o1.turn()  # 7
    o1.jump()  # 0
    o1.bend()  # 2
    o1.bend()  # 4
    o1.jump()  # 5
    o1.jump()  # 6
    try:
        o1.jump()
    except MealyError:
        pass
    try:
        o1.bend()
    except MealyError:
        pass
    try:
        o1.turn()
    except MealyError:
        pass


test()