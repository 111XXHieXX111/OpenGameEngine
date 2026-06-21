from ...Core.glob import log_system
from .polygon import Polygon
from .base import Base
from .modules import *

class Triangle(Base):
    def __init__(self):
        log_system.addInfo("Figure: create triangle")
        self.vertexes = [Vec2(0.0, 0.0), Vec2(0.0, 0.0), Vec2(0.0, 0.0)]
        self.position = Vec2(0.0, 0.0)
        self.size = Vec2(0.0, 0.0)
        self.rotation = Vec1(0.0)
        self.color = Color4(0.0, 0.0, 0.0, 0.0)
        self.widthlines = Vec1(1.0)
        self.pointsize = Vec1(1.0)
        self.uv = [Vec2(0, 0), Vec2(1, 0), Vec2(0.5, 1)]
        self.texture = None
        self.calculated = False

    def calculateSize(self):
        center = Vec2(
            self.position.x + self.size.x / 2,
            self.position.y + self.size.y / 2
        )
        
        angle = math.radians(self.rotation.x)
        
        cos_angle = math.cos(angle)
        sin_angle = math.sin(angle)

        corners = [
            Vec2(center.x, center.y - self.size.y / 2),
            Vec2(center.x - self.size.x / 2, center.y + self.size.y / 2),
            Vec2(center.x + self.size.x / 2, center.y + self.size.y / 2)
        ]

        for i in range(3):
            corners[i].x -= center.x
            corners[i].y -= center.y

        for i in range(3):
            x_new = corners[i].x * cos_angle - corners[i].y * sin_angle
            y_new = corners[i].x * sin_angle + corners[i].y * cos_angle
            self.vertexes[i] = Vec2(x_new, y_new)

        for i in range(3):
            self.vertexes[i].plusVector(center)

        self.calculated = True
    
    def drawTriangle(self, mode:drawMode):
        self.draw("Triangle")
        
        if not self.calculated:
            self.calculateSize()
            return
        
        polygon = Polygon(self.vertexes)
        polygon.setColor(self.color)
        polygon.setWidthLines(self.widthlines)
        polygon.setPointSize(self.pointsize)
        polygon.setTexCoords(self.uv)
        polygon.setTexture(self.texture)
        polygon.drawPolygon(mode)