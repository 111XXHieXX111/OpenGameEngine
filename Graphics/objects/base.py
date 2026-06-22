from .modules import *
from ...Core.glob import log_system, render_items
from ...Core.base import System

class Base:
    def setPointSize(self, new_size:Vec1):
        
        # CHECK
        
        if isinstance(new_size, int) or isinstance(new_size, float):
            log_system.addWarn("Use Vec1 in setPointSize")
            new_size = Vec1(new_size)
        else:
            if not isinstance(new_size, Vec1):
                log_system.addError("Use Vec1 in setPointSize")
                return
        
        # APPLY
        
        self.pointsize = new_size

    def setWidthLines(self, new_width:Vec1):
        
        # CHECK
        
        if isinstance(new_width, int) or isinstance(new_width, float):
            log_system.addWarn("Use Vec1 in setWidthLines")
            new_width = Vec1(new_width)
        else:
            if not isinstance(new_width, Vec1):
                log_system.addError("Use Vec1 in setWidthLines")
                return
        
        # APPLY
        
        self.widthlines = new_width
    
    def setSize(self, new_size:Vec2):
        
        # CHECK TYPE
        
        if isinstance(new_size, list) or isinstance(new_size, tuple):
            new_size = System.cltv2(new_size)
            log_system.addWarn("Use Vec2 in setSize")
        else:
            if not isinstance(new_size, Vec2):
                return
        
        # APPLY
        
        self.size = new_size
        self.calculated = False
    
    def setPosition(self, new_position:Vec2):
        
        # CHECK TYPE
        
        if isinstance(new_position, list) or isinstance(new_position, tuple):
            new_position = System.cltv2(new_position)
        else:
            if not isinstance(new_position, Vec2):
                return
        
        # APPLY
        
        self.position = new_position
        self.calculated = False
    
    def setRotation(self, new_rotation:Vec1):
        
        # CHECK TYPE
        
        if isinstance(new_rotation, int):
            new_rotation = Vec1(new_rotation)
        else:
            if not isinstance(new_rotation, Vec1):
                return
        
        # APPLY
        
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

    def _draw(self, name:str):
        render_items.append(name)