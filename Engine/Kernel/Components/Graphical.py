from .Vectors import Vec3
import ctypes

class c256:
    def __new__(cls, x:float | int):
        return x / 256

class Color3:
    __slots__ = ("r", "g", "b")
    
    def __init__(self, r:float | int, g:float | int, b:float | int):
        self.r, self.g, self.b = r, g, b
    
    def __add__(self, other):
        return Color3(self.r + other.r, self.g + other.g, self.b + other.b)

    def __sub__(self, other):
        return Color3(self.r - other.r, self.g - other.g, self.b - other.b)
    
    def __mul__(self, scalar):
        return Color3(self.r * scalar.r, self.g * scalar.g, self.b * scalar.b)
    
    def __truediv__(self, scalar):
        return Color3(self.r / scalar.r, self.g / scalar.g, self.b / scalar.b)

class Color4:
    __slots__ = ("r", "g", "b", "a")
    
    def __init__(self, r:float | int, g:float | int, b:float | int, a:float | int):
        self.r, self.g, self.b, self.a = r, g, b, a
    
    def __add__(self, other):
        return Color4(self.r + other.r, self.g + other.g, self.b + other.b, self.a + other.a)

    def __sub__(self, other):
        return Color4(self.r - other.r, self.g - other.g, self.b - other.b, self.a - other.a)
    
    def __mul__(self, scalar):
        return Color4(self.r * scalar.r, self.g * scalar.g, self.b * scalar.b, self.a * scalar.a)
    
    def __truediv__(self, scalar):
        return Color4(self.r / scalar.r, self.g / scalar.g, self.b / scalar.b, self.a / scalar.a)

class Vertex(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("z", ctypes.c_float),
        ("r", ctypes.c_float),
        ("g", ctypes.c_float),
        ("b", ctypes.c_float),
        ("a", ctypes.c_float),
    ]

    def __init__(self, position:Vec3, color:Color4):
        self.x = position.x
        self.y = position.y
        self.z = position.z
        self.r = color.r
        self.g = color.g
        self.b = color.b
        self.a = color.a

def c3toc4(Color:Color3 | Color4):
    if isinstance(Color, Color4):
        return Color

    return Color4(Color.r, Color.g, Color.b, 1.0)
