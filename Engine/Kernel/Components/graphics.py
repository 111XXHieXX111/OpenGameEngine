from ..modules import GL, Enum

class shaderType:
    VERTEX = GL.GL_VERTEX_SHADER
    FRAGMENT = GL.GL_FRAGMENT_SHADER

class batchDrawing:
    DYNAMIC = "DYNAMIC"
    STATIC = "STATIC"

class textureType:
    LINEAR = GL.GL_LINEAR
    NEAREST = GL.GL_NEAREST

class stretchType(Enum):
    EXPAND = "EXPAND"
    RELATIVELY = "RELATIVELY"
    KEEP_ASPECT = "KEEP_ASPECT"

class drawMode:
    POINTS = GL.GL_POINTS
    LOOP = GL.GL_LINE_LOOP
    FORM = GL.GL_TRIANGLE_STRIP
    FILL = GL.GL_POLYGON
    RECT = GL.GL_QUADS

# COLORS

class c256:
    def __new__(cls, x:float):
        return x / 256

class Color3:
    __slots__ = ("r", "g", "b")
    
    def __init__(self, r:float | c256, g:float | c256, b:float | c256):
        self.r, self.g, self.b = r, g, b

    def getColor(self):
        return self.r, self.g, self.b

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
    
    def __init__(self, r:float | c256, g:float | c256, b:float | c256, a:float | c256):
        self.r, self.g, self.b, self.a = r, g, b, a

    def getColor(self):
        return self.r, self.g, self.b, self.a
    
    def __add__(self, other):
        return Color4(self.r + other.r, self.g + other.g, self.b + other.b, self.a + other.a)

    def __sub__(self, other):
        return Color4(self.r - other.r, self.g - other.g, self.b - other.b, self.a - other.a)
    
    def __mul__(self, scalar):
        return Color4(self.r * scalar.r, self.g * scalar.g, self.b * scalar.b, self.a * scalar.a)
    
    def __truediv__(self, scalar):
        return Color4(self.r / scalar.r, self.g / scalar.g, self.b / scalar.b, self.a / scalar.a)

# ANIMATIONS

class Animation:
    def __init__(self, name:str, frames:list[int] | tuple[int], interval:int | float, loop:bool):
        self.name = name
        self.frames = frames
        self.interval = 0.0
        self.loop = loop
