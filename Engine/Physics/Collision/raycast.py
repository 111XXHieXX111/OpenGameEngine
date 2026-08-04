from ...Kernel.Components.graphics import Color4
from ...Kernel.Components.vectors import Vec2
from ...Graphics.Primitives.line import Line
from .Globals.aabb import _GAABB

class Ray:
    def __init__(self, vertexes):
        self.vertexes = vertexes

class rayCast:
    def __init__(self, ignores:list=[]):
        self.pos1 = Vec2(0.0, 0.0)
        self.pos2 = Vec2(0.0, 0.0)
        self.ignores = ignores
        self.colliding = False

    def setPositions(self, pos1:Vec2, pos2:Vec2):
        self.pos1 = pos1
        self.pos2 = pos2

    def rayCastProcess(self):
        self.colliding = False
        if _GAABB(Ray([self.pos1, self.pos2]), self.ignores):
            self.colliding = True

    def rayCastDraw(self):
        line = Line()
        line.setPoint1(self.pos1)
        line.setPoint2(self.pos2)
        line.setColor(Color4(0.0, 1.0, 1.0, 0.8))
        line.drawLine()
