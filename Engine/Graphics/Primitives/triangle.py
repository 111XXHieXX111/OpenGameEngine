from ...Kernel.kernel import classWrapper
from .polygon import PolygonLegacy, Polygon
from .base import Base
from .modules import *

@classWrapper
class Triangle(Base):
    def __init__(self, window=None):
        super().__init__()
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
        self.window = window
        self.shader = None
        if self.window.render_type == 0:
            self.polygon = Polygon(self.vertexes, self.window)
        else:
            self.polygon = PolygonLegacy(self.vertexes)

    def calculateSize(self):
        center = Vec2(
            self.position.x + self.size.x / 2,
            self.position.y + self.size.y / 2
        )
        
        angle = radians(self.rotation.x)
        
        cos_angle = cos(angle)
        sin_angle = sin(angle)

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
            self.vertexes[i] += center

        self.polygon.setVertexes(self.vertexes)

        self.calculated = True
    
    def drawTriangle(self, mode:drawMode):
        
        # Optimization
        
        if not self._in_window():
            return
        
        self._draw("Triangle")
        
        if not self.calculated:
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
