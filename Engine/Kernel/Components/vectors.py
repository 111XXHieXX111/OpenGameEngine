class Vec2:
    __slots__ = ("x", "y")
    
    def __init__(self, x:int | float, y:int | float):
        self.x = x
        self.y = y
    
    def getVectors(self):
        return self.x, self.y
    
    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vec2(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        return Vec2(self.x / scalar, self.y / scalar)

class Vec1:
    __slots__ = ("x",)
    
    def __init__(self, x:int | float):
        self.x = x
    
    def getVectors(self):
        return self.x

    def __add__(self, other):
        return Vec1(self.x + other.x)
    
    def __sub__(self, other):
        return Vec1(self.x - other.x)
    
    def __mul__(self, scalar):
        return Vec1(self.x * scalar.x)
    
    def __truediv__(self, scalar):
        return Vec1(self.x / scalar.x)
