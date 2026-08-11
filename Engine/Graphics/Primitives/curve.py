from .modules import *
from .base import linedBase
from .line import Line

class Curve(linedBase):
    def __init__(self, window):
        super().__init__()
        self.points = []
        self.color = Color4(0.0, 0.0, 0.0, 0.0)
        self.widthlines = Vec1(1.0)
        self.pointsize = Vec1(1.0)
        self.shader = None
        self.window = window
        self.lines = []
        self.calculated = False

    def addPoint(self, position:Vec2):
        self.points.append(position)
        self.calculated = False

    def removePointByPosition(self, position:Vec2):
        self.points.remove(position)
        self.calculated = False

    def removePointByIndex(self, index:int):
        self.points.pop(index)
        self.calculated = False

    def clearPoints(self):
        self.points.clear()
        self.calculated = False

    def calculateSize(self):
        if len(self.points) > 1:
            self.lines.clear()

            for index, point in enumerate(self.points):
                line = Line(self.window)

                if index+1 > len(self.points)-1:
                    break

                nxt = self.points[index+1]

                line.setPoint1(Vec2(point.x, point.y))
                line.setPoint2(Vec2(nxt.x, nxt.y))
                
                line.setColor(self.color)
                line.setWidthLines(self.widthlines)
                line.setPointSize(self.pointsize)

                self.lines.append(line)

        self.calculated = True

    def drawCurve(self):
        self._draw(self)

        if not self.calculated:
            self.calculateSize()

        for line in self.lines:
            line.drawLine()
