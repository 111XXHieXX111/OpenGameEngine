from ...Kernel.kernel import log_system, render_items
from ...Kernel.Components.system import System
from .polygon import PolygonLegacy
from .modules import *
from .object import GFXObject

class Line(GFXObject):
    def __init__(self, window):
        super().__init__()
        self.point_1 = Vec2(0.0, 0.0)
        self.point_2 = Vec2(0.0, 0.0)
        self.color = Color4(0.0, 0.0, 0.0, 0.0)
        self.widthlines = Vec1(1.0)
        self.pointsize = Vec1(1.0)
        self.shader = None
        self.polygon = PolygonLegacy([Vec2(0.0, 0.0), Vec2(0.0, 0.0)])
        self.calculated = False
        self.window = window
    
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

    def calculateSize(self):
        self.polygon.vertexes = [self.point_1, self.point_2]
        self.polygon.setColor(self.color)
        self.polygon.setPointSize(self.pointsize)
        self.polygon.setWidthLines(self.widthlines)
        self.calculated = True

    def drawLine(self):
        render_items.append("Line")

        if not self.calculated:
            self.calculateSize()

        if self.shader:
            GL.glUseProgram(self.shader.program)
            self.shader._apply_uniforms()
        
        self.polygon.drawPolygon(drawMode.LINES)

        if self.shader:
            GL.glUseProgram(0)

        if self.window:
            if self.window.debugmenu == 3:
                self.window.drawText(f"ID:{self.id}", self.point_1, debug_only=True)
