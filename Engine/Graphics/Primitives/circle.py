from .polygon import PolygonLegacy, Polygon
from .base import Base
from .modules import *

@classWrapper
class Circle(Base):
    def __init__(self, segments=8, window=None):
        super().__init__()
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
        self.window = window
        self.shader = None
        if self.window.render_type == 0:
            self.polygon = Polygon(self.vertexes, self.window)
        else:
            self.polygon = PolygonLegacy(self.vertexes)
    
    def calculateSize(self):
        if not self._dirty and self._cached_vertices is not None:
            self.vertexes = self._cached_vertices.copy()
            return
        
        if not hasattr(self, "_angles") or len(self._angles) != self.segments:
            self._angles = [2 * PI * i / self.segments for i in range(self.segments)]
        
        half_x = self.size.x / 2
        half_y = self.size.y / 2
        
        self.uv = []
        
        for i, angle in enumerate(self._angles):
            self.vertexes[i].x = (cos(angle) * half_x) + self.position.x
            self.vertexes[i].y = (sin(angle) * half_y) + self.position.y
            
            u = (cos(angle) + 1) / 2
            v = (sin(angle) + 1) / 2
            self.uv.append(Vec2(u, v))
        
        self._cached_vertices = self.vertexes.copy()
        self._dirty = False

        self.polygon.setVertexes(self.vertexes)

    def drawCircle(self, mode:drawMode):
        
        # Optimization
        
        if not self._in_window():
            return
        
        self._draw("Circle")
        if self._dirty or self._cached_vertices is None:
            self.calculateSize()
        
        if self.shader:
            GL.glUseProgram(self.shader.program)
            self.shader._apply_uniforms()
        
        if self.window.render_type == 1:
            self.polygon.setColor(self.color)
            self.polygon.setWidthLines(self.widthlines)
            self.polygon.setPointSize(self.pointsize)
            self.polygon.setTexCoords(self.uv)
            self.polygon.setTexture(self.texture)
            self.polygon.drawPolygon(mode)
        else:
            self.polygon.vertexes = self.vertexes
            self.polygon.setColor(self.color)
            self.polygon.setTexCoords(self.uv)
            self.polygon.setTexture(self.texture)
            self.polygon.drawPolygon(mode)
        
        if self.shader:
            GL.glUseProgram(0)
