from .modules import GL, Enum, glfw
from .glob import log_system

# VECTORS

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

# COLOR

class c256:
    def __new__(cls, x:float):
        return x / 256

class Color3:
    __slots__ = ("r", "g", "b")
    
    def __init__(self, r:float | c256, g:float | c256, b:float | c256):
        self.r, self.g, self.b = r, g, b

    def getColor(self):
        return self.r, self.g, self.b

class Color4:
    __slots__ = ("r", "g", "b", "a")
    
    def __init__(self, r:float | c256, g:float | c256, b:float | c256, a:float | c256):
        self.r, self.g, self.b, self.a = r, g, b, a

    def getColor(self):
        return self.r, self.g, self.b, self.a

# BINDS

class Key:
    __slots__ = ("key")
    
    def __init__(self, key:str):
        self.key = key
    
    def getKey(self):
        return self.key

class MouseButton:
    LEFT = glfw.MOUSE_BUTTON_LEFT
    RIGHT = glfw.MOUSE_BUTTON_RIGHT
    MIDDLE = glfw.MOUSE_BUTTON_MIDDLE
    BUTTON_4 = glfw.MOUSE_BUTTON_4
    BUTTON_5 = glfw.MOUSE_BUTTON_5
    BUTTON_6 = glfw.MOUSE_BUTTON_6
    BUTTON_7 = glfw.MOUSE_BUTTON_7
    BUTTON_8 = glfw.MOUSE_BUTTON_8

# SYSTEM

class System:
    @staticmethod
    def check_empty(text:str):
        replaced_text = text.replace(' ', '')
        return replaced_text == ''

    @staticmethod
    def c3toc4(color:Color3 | Color4, a:float | c256 = 1.0):
        if isinstance(color, Color3):
            return Color4(color.r, color.g, color.b, a)
        elif isinstance(color, Color4):
            return Color4(color.r, color.g, color.b, color.a if a == 1.0 else a)
        else:
            log_system.addWarn("Use Color3|Color4")
            return Color4(0, 0, 0, 1)
    
    @staticmethod
    def slfm(x:int | float, y:int | float):
        return abs(x - y)

    @staticmethod
    def cltv2(l:list|tuple):
        if len(l) > 1:
            return Vec2(l[0], l[1])

# DRAWING

class drawMode:
    POINTS = GL.GL_POINTS
    LOOP = GL.GL_LINE_LOOP
    FORM = GL.GL_TRIANGLE_STRIP
    FILL = GL.GL_POLYGON
    RECT = GL.GL_QUADS

# SHADERS

class shaderType:
    VERTEX = GL.GL_VERTEX_SHADER
    FRAGMENT = GL.GL_FRAGMENT_SHADER

# BATCH

class batchDrawing:
    DYNAMIC = "DYNAMIC"
    STATIC = "STATIC"

# TEXTURES

class textureType:
    LINEAR = GL.GL_LINEAR
    NEAREST = GL.GL_NEAREST

# WINDOW

class stretchType(Enum):
    EXPAND = "EXPAND"
    RELATIVELY = "RELATIVELY"
    KEEP_ASPECT = "KEEP_ASPECT"