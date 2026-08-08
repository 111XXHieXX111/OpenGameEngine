from .Components.vectors import Vec2
from .modules import overload, random
from .kernel import classWrapper

PI = 3.141592

def sin(x):
    x = x % (2 * PI)
    if x > PI:
        x -= 2 * PI
    
    result = 0
    term = x
    for n in range(10):
        result += term
        term = term * (-x * x) / ((2*n + 2) * (2*n + 3))
    return result

def cos(x):
    x = x % (2 * PI)
    if x > PI:
        x -= 2 * PI
    
    result = 0
    term = 1
    for n in range(10):
        result += term
        term = term * (-x * x) / ((2*n + 1) * (2*n + 2))
    return result

def radians(degrees):
    return degrees * PI / 180

@classWrapper
class Math:
    @staticmethod
    def Clamp(x:int|float, y:int|float, value:int|float):
        if value < x:
            return x
        elif value > y:
            return y
        return value

    @staticmethod
    def clampVec2(x:int|float, y:int|float, vector:Vec2):
        x = Math.Clamp(x, y, vector.x)
        y = Math.Clamp(x, y, vector.y)
        return Vec2(x, y)

    @staticmethod
    def getDistanceVec2(x:Vec2, y:Vec2):
        dx = x.x - y.x
        dy = x.y - y.y
        return (dx*dx + dy*dy)**0.5

    @staticmethod
    def Lerp(a:str | float, b:str | float, t:int | float):
        return a + (b - a) * t

@classWrapper
class Random:
    @overload
    def randomNum(x:int, y:int) -> int: ...

    @overload
    def randomNum(x:float, y:float) -> float: ...

    @staticmethod
    def randomNum(x, y):
        if isinstance(x, int) and isinstance(y, int):
            return random.randint(x, y)
        elif isinstance(x, float) and isinstance(y, float):
            return random.uniform(x, y)
    
    @staticmethod
    def randomBool():
        return bool(Random.randomNum(0, 1))

    @staticmethod
    def randomChoice(x:list):
        return random.choice(x)
