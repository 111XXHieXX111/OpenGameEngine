from .modules import *
from ...Kernel.kernel import log_system, render_items, classWrapper
from ...Kernel.Components.system import System
from ...Kernel.Components.graphics import stretchType
from ...Graphics.Utils.shader import Shader
from .object import GFXObject

@classWrapper
class Base(GFXObject):
    __slots__ = ("vertexes", "position", "size", "rotation", "color", "widthlines", "pointsize", "uv", "texture", "calculated", "window", "shader", "segments", "_dirty", "_cached_vertices")
    
    def __init__(self):
        super().__init__()

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
        self.calculated = False

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
        self.calculated = False
    
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
        self.calculated = False
    
    def setUV(self, uv:list[Vec2] | tuple[Vec2]):
        self.uv = uv
        self.calculated = False
    
    def setTexture(self, texture):
        self.texture = texture
        self.calculated = False
    
    def setShader(self, shader:Shader):
        self.shader = shader
        self.calculated = False
    
    def getCenter(self):
        xs, ys = [], []
        for v in self.vertexes:
            xs.append(v.x)
            ys.append(v.y)
        return Vec2(sum(xs) / len(xs), sum(ys) / len(ys))

    def _draw(self, name:str):
        render_items.append(name)

    def _in_window(self):
        if self.window:
            if not self.window.camera["enabled"]:
                if self.window.window_settings["stretch"] != stretchType.RELATIVELY:
                    winsize = [self.window.window_settings["width"], self.window.window_settings["height"]]
                else:
                    winsize = self.window.current_window_sizes
                
                if self.position.x + self.size.x <= 0 or self.position.y + self.size.y <= 0:
                    return False
                if self.position.x >= winsize[0] or self.position.y >= winsize[1]:
                    return False
        return True

class linedBase(GFXObject):
    def __init__(self):
        super().__init__()

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
        self.calculated = False

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
        self.calculated = False
    
    def setColor(self, new_color:Color3 | Color4):
        self.color = System.c3toc4(new_color)
        self.calculated = False

    def setShader(self, shader:Shader):
        self.shader = shader
        self.calculated = False

class Pointed:
    def setPoint1(self, new_position:Vec2):
        if isinstance(new_position, list) or isinstance(new_position, tuple):
            new_position = System.cltv2(new_position)
        else:
            if not isinstance(new_position, Vec2):
                return
        
        self.point_1 = new_position
        self.calculated = False
    
    def setPoint2(self, new_position:Vec2):
        if isinstance(new_position, list) or isinstance(new_position, tuple):
            new_position = System.cltv2(new_position)
        else:
            if not isinstance(new_position, Vec2):
                return
        
        self.point_2 = new_position
        self.calculated = False
