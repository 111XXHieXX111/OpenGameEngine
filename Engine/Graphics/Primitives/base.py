from .modules import *
from ...Kernel.kernel import log_system, render_items, classWrapper
from ...Kernel.Components.system import System
from ...Kernel.Components.graphics import stretchType
from ...Graphics.Utils.shader import Shader
from ...Misc.manager import Manager
from ...Kernel.math import cos, sin, radians
from .object import GFXObject

@classWrapper
class canParent(Manager):
    def __init__(self):
        self.objs = []

    def getChildrens(self):
        return self.objs

    def getChild(self, name:str):
        index, child = self._find(name)
        if child:
            return child

        log_system.addError(f"Children:{name} is not found!")
        return None

    def addChild(self, name:str, obj):
        index, child = self._find(name)
        if child:
            log_system.addError(f"Children:{name} with this name already exists")
            return

        self.objs.append([name, obj, Vec2((obj.position.x - self.position.x) / self.size.x, (obj.position.y - self.position.y) / self.size.y), Vec2(obj.size.x / self.size.x, obj.size.y / self.size.y), obj.rotation])
            
    def removeChild(self, name:str):
        index, child = self._find(name)
        if index and child:
            self.objs.remove(self.objs[index])
        else:
            log_system.addError(f"Child:{name} is not found!")
    
    def childrensProcess(self):
        if not self.objs:
            return

        angle = radians(self.rotation.x)
        cos_a = cos(angle)
        sin_a = sin(angle)

        for child in self.objs:
            lx, ly = child[2].x, child[2].y
            
            scaled_lx = lx * self.size.x
            scaled_ly = ly * self.size.y
            
            rx = scaled_lx * cos_a - scaled_ly * sin_a
            ry = scaled_lx * sin_a + scaled_ly * cos_a

            child[1].setPosition(self.position + Vec2(rx, ry))
            child[1].setSize(Vec2(self.size.x * child[3].x, self.size.y * child[3].y))
            child[1].setRotation(self.rotation + child[4])

@classWrapper
class Base(GFXObject, canParent):
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
        self.childrensProcess()
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

@classWrapper
class linedBase(GFXObject, canParent):
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

    def _draw(self, name:str):
        self.childrensProcess()
        render_items.append(name)

@classWrapper
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
