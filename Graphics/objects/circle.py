from ...Core.glob import log_system
from .polygon import Polygon
from .base import Base
from .modules import *

class Circle(Base):
    def __init__(self):
        log_system.addInfo("Figure: create circle")
        self.vertexes = [Vec2(0.0, 0.0) for _ in range(360)]
        self.position = Vec2(0.0, 0.0)
        self.size = Vec2(0.0, 0.0)
        self.rotation = Vec1(0.0)
        self.color = Color4(0.0, 0.0, 0.0, 0.0)
        self.widthlines = Vec1(1.0)
        self.uv = []
        self.texture = None
        self.calculated = False
    
    def calculateSize(self):
        self.uv = []
        for i in range(360):
            angle = 2 * math.pi * i / 360
            u = (math.cos(angle) + 1) / 2
            v = (math.sin(angle) + 1) / 2
            self.uv.append(Vec2(u, v))

        for i, v in enumerate(self.vertexes):
            angle = 2 * math.pi * i / 360
            v.x = (math.cos(angle) * self.size.x / 2) + self.position.x
            v.y = (math.sin(angle) * self.size.y / 2) + self.position.y
        
        self.calculated = True

    def drawCircle(self, mode:drawMode):
        self.draw("Circle")
        
        if not self.calculated:
            self.calculateSize()
            return
        
        polygon = Polygon(self.vertexes)
        polygon.setColor(self.color)
        polygon.setWidthLines(self.widthlines)
        polygon.setTexCoords(self.uv)
        polygon.setTexture(self.texture)
        polygon.drawPolygon(mode)