from .modules import *
from ...Core.glob import log_system

class Base:
    def __init__(self):
        log_system.addInfo("Base: creating figure")

    def setWidthLines(self, new_width:Vec1):
        self.widthlines = new_width
    
    def setSize(self, new_size:Vec2):
        self.size = new_size
        self.calculated = False
    
    def setPosition(self, new_position:Vec2):
        self.position = new_position
        self.calculated = False
    
    def setRotation(self, new_rotation:Vec1):
        self.rotation = new_rotation
        self.calculated = False
    
    def setColor(self, new_color:Color3 | Color4):
        self.color = System.c3toc4(new_color)
    
    def setUV(self, uv:list[Vec2] | tuple[Vec1]):
        self.uv = uv
    
    def setTexture(self, texture):
        self.texture = texture
    
    def getCenter(self):
        xs, ys = [], []
        for v in self.vertexes:
            xs.append(v.x)
            ys.append(v.y)
        return Vec2(sum(xs) / len(xs), sum(ys) / len(ys))