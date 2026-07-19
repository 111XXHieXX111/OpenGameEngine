from ...Kernel.kernel import render_items
from ...Kernel.Components.system import System
from .line import Line
from .modules import *
from .base import linedBase, Pointed

@classWrapper
class Arrow(linedBase, Pointed):
    def __init__(self, window=None):
        super().__init__()
        self.point_1 = Vec2(0.0, 0.0)
        self.point_2 = Vec2(0.0, 0.0)
        self.color = Color4(0.0, 0.0, 0.0, 0.0)
        self.widthlines = Vec1(1.0)
        self.pointsize = Vec1(1.0)
        self.shader = None
        self.lines = [Line(window), Line(window), Line(window)]
        self.calculated = False
        self.window = window

    def calculateSize(self):
        self.lines[0].setPoint1(self.point_1)
        self.lines[0].setPoint2(self.point_2)

        dx = self.point_2.x - self.point_1.x
        dy = self.point_2.y - self.point_1.y
    
        length = (dx*dx + dy*dy) ** 0.5
        if length > 0:
            dx /= length
            dy /= length
    
        size = length/16
    
        px = -dy * size
        py = dx * size
    
        self.lines[1].setPoint1(self.point_2)
        self.lines[1].setPoint2(Vec2(self.point_2.x - dx*size + px, self.point_2.y - dy*size + py))
    
        self.lines[2].setPoint1(self.point_2)
        self.lines[2].setPoint2(Vec2(self.point_2.x - dx*size - px, self.point_2.y - dy*size - py))

        for line in self.lines:
            line.setColor(self.color)
            line.setWidthLines(self.widthlines)
            line.setShader(self.shader)

        self.calculated = True

    def drawArrow(self):
        self._draw("Arrow")

        if not self.calculated:
            self.calculateSize()

        if self.shader:
            GL.glUseProgram(self.shader.program)
            self.shader._apply_uniforms()

        for line in self.lines:
            line.drawLine()

        if self.shader:
            GL.glUseProgram(0)

        if self.window:
            if self.window.debugmenu == 3:
                self.window.drawText(f"ID:{self.id}", self.point_1, debug_only=True)
