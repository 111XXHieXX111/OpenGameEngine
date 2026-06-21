from .modules import GL, Enum
from .glob import log_system

# VECTORS

class Vec2:
    def __init__(self, x:int | float, y:int | float):
        self.x = x
        self.y = y
    
    def plusVector(self, vector):
        self.x += vector.x
        self.y += vector.y
    
    def getVectors(self):
        return self.x, self.y

class Vec1:
    def __init__(self, x:int | float):
        self.x = x
    
    def getVectors(self):
        return self.x

# COLOR

class c256:
    def __new__(cls, x: float):
        return x / 256

class Color3:
    def __init__(self, r:float | c256, g:float | c256, b:float | c256):
        self.r, self.g, self.b = r, g, b

    def getColor(self):
        return self.r, self.g, self.b

class Color4:
    def __init__(self, r:float | c256, g:float | c256, b:float | c256, a:float | c256):
        self.r, self.g, self.b, self.a = r, g, b, a

    def getColor(self):
        return self.r, self.g, self.b, self.a

# BINDS

class Key:
    def __init__(self, key:str):
        self.key = key
    
    def getKey(self):
        return self.key

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
        else:
            if not isinstance(color, Color3) and not isinstance(color, Color4):
                log_system.addWarn("Use Color3|Color4")
                return Color4(0, 0, 0, 1)
    
        return color
    
    @staticmethod
    def slfm(x:int | float, y:int | float):
        return abs(x - y)

    @staticmethod
    def cltv2(l:list|tuple):
        if len(l) > 1:
            return Vec2(l[0], l[1])

# DRAWING

class drawMode(Enum):
    POINTS = GL.GL_POINTS
    LOOP = GL.GL_LINE_LOOP
    FORM = GL.GL_TRIANGLE_STRIP
    FILL = GL.GL_POLYGON
    RECT = GL.GL_QUADS

# SHADERS

class shaderType:
    VERTEX = GL.GL_VERTEX_SHADER
    FRAGMENT = GL.GL_FRAGMENT_SHADER

# TEXTURES

class textureType:
    LINEAR = GL.GL_LINEAR
    NEAREST = GL.GL_NEAREST

# WINDOW

class stretchType(Enum):
    EXPAND = "EXPAND"
    RELATIVELY = "RELATIVELY"
    KEEP_ASPECT = "KEEP_ASPECT"