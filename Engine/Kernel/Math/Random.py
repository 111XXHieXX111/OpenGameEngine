from ..Components.Graphical import Color3, Color4
from ..Kernel import ClassWrapper
from typing import overload
import random

@ClassWrapper
class Random:
    @overload
    def RandomNum(x:int, y:int) -> int: ...

    @overload
    def RandomNum(x:float, y:float) -> float: ...

    @staticmethod
    def RandomNum(x, y):
        if isinstance(x, int) and isinstance(y, int):
            return random.randint(x, y)
        elif isinstance(x, float) and isinstance(y, float):
            return random.uniform(x, y)
    
    @staticmethod
    def RandomBool():
        return bool(Random.RandomNum(0, 1))

    @staticmethod
    def RandomChoice(x:list):
        return random.choice(x)

    @staticmethod
    def RandomColor3():
        return Color3(
            Random.RandomNum(0.0, 1.0),
            Random.RandomNum(0.0, 1.0),
            Random.RandomNum(0.0, 1.0)
        )

    @staticmethod
    def RandomColor4(rnd_alpha:bool=False):
        if rnd_alpha:
            return Color4(
                Random.RandomNum(0.0, 1.0),
                Random.RandomNum(0.0, 1.0),
                Random.RandomNum(0.0, 1.0),
                Random.RandomNum(0.0, 1.0)
            )
        else:
            return Color4(
                Random.RandomNum(0.0, 1.0),
                Random.RandomNum(0.0, 1.0),
                Random.RandomNum(0.0, 1.0),
                1.0
            )
