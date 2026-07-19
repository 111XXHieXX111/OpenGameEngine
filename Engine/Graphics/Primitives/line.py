from ...Kernel.kernel import render_items
from ...Kernel.Components.system import System
from .polygon import PolygonLegacy
from .modules import *
from .base import linedBase, Pointed

class Line(linedBase, Pointed):
    def __init__(self, window=None):
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
