from ...Core.glob import log_system
from .polygon import Polygon
from .base import Base
from .modules import *

class Rectangle(Base):
    def __init__(self):
        self.vertexes = [Vec2(0.0, 0.0), Vec2(0.0, 0.0), Vec2(0.0, 0.0), Vec2(0.0, 0.0)]
        self.position = Vec2(0.0, 0.0)
        self.size = Vec2(0.0, 0.0)
        self.rotation = Vec1(0.0)
        self.color = Color4(0.0, 0.0, 0.0, 0.0)
        self.widthlines = Vec1(1.0)
        self.pointsize = Vec1(1.0)
        self.uv = [Vec2(0, 0), Vec2(1, 0), Vec2(1, 1), Vec2(0, 1)]
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

        half_width = self.size.x / 2
        half_height = self.size.y / 2
        
        corners = [
            Vec2(-half_width, -half_height),
            Vec2(half_width, -half_height),
            Vec2(half_width, half_height),
            Vec2(-half_width, half_height)
        ]

        for i in range(4):
            x_new = corners[i].x * cos_angle - corners[i].y * sin_angle
            y_new = corners[i].x * sin_angle + corners[i].y * cos_angle
            self.vertexes[i] = Vec2(x_new + center.x, y_new + center.y)

        self.calculated = True
    
    def drawRectangle(self, mode:drawMode):
        self._draw("Rectangle")
        
        if not self.calculated:
            self.calculateSize()
        
        polygon = Polygon(self.vertexes)
        polygon.setColor(self.color)
        polygon.setWidthLines(self.widthlines)
        polygon.setPointSize(self.pointsize)
        polygon.setTexCoords(self.uv)
        polygon.setTexture(self.texture)
        polygon.drawPolygon(mode)
