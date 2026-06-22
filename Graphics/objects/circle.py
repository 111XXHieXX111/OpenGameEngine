from ...Core.glob import log_system
from .polygon import Polygon
from .base import Base
from .modules import *

class Circle(Base):
    def __init__(self, segments=8):
        self.segments = segments
        self.vertexes = [Vec2(0.0, 0.0) for _ in range(segments)]
        self.position = Vec2(0.0, 0.0)
        self.size = Vec2(0.0, 0.0)
        self.rotation = Vec1(0.0)
        self.color = Color4(0.0, 0.0, 0.0, 0.0)
        self.widthlines = Vec1(1.0)
        self.pointsize = Vec1(1.0)
        self.uv = [Vec2(0.0, 0.0) for _ in range(segments)]
        self.texture = None
        self._dirty = True
        self._cached_vertices = None
    
    def calculateSize(self):
        if not self._dirty and self._cached_vertices is not None:
            self.vertexes = self._cached_vertices.copy()
            return
        
        if not hasattr(self, "_angles") or len(self._angles) != self.segments:
            self._angles = [2 * math.pi * i / self.segments for i in range(self.segments)]
        
        half_x = self.size.x / 2
        half_y = self.size.y / 2
        
        self.uv = []
        
        for i, angle in enumerate(self._angles):
            self.vertexes[i].x = (math.cos(angle) * half_x) + self.position.x
            self.vertexes[i].y = (math.sin(angle) * half_y) + self.position.y
            
            u = (math.cos(angle) + 1) / 2
            v = (math.sin(angle) + 1) / 2
            self.uv.append(Vec2(u, v))
        
        self._cached_vertices = self.vertexes.copy()
        self._dirty = False

    def drawCircle(self, mode:drawMode):
        self._draw("Circle")
        if self._dirty or self._cached_vertices is None:
            self.calculateSize()
        
        polygon = Polygon(self.vertexes)
        polygon.setColor(self.color)
        polygon.setWidthLines(self.widthlines)
        polygon.setPointSize(self.pointsize)
        polygon.setTexCoords(self.uv)
        polygon.setTexture(self.texture)
        polygon.drawPolygon(mode)