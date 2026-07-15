from .polygon import PolygonLegacy, Polygon
from .base import Base
from .modules import *

@classWrapper
class Rectangle(Base):
    def __init__(self, window=None):
        super().__init__()
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
        self.window = window
        self.shader = None
    
    def calculateSize(self):
        center = Vec2(
            self.position.x + self.size.x / 2,
            self.position.y + self.size.y / 2
        )
        
        angle = radians(self.rotation.x)
        
        cos_angle = cos(angle)
        sin_angle = sin(angle)

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
        
        # Optimization
        
        if not self._in_window():
            return
        
        self._draw("Rectangle")
        
        if not self.calculated:
            self.calculateSize()
        
        if self.shader:
            GL.glUseProgram(self.shader.program)
            self.shader._apply_uniforms()

        if self.window.render_type == 1:
            polygon = PolygonLegacy(self.vertexes)
            polygon.setColor(self.color)
            polygon.setWidthLines(self.widthlines)
            polygon.setPointSize(self.pointsize)
            polygon.setTexCoords(self.uv)
            polygon.setTexture(self.texture)
            polygon.drawPolygon(mode)
        elif self.window.render_type == 0:
            polygon = Polygon(self.vertexes.copy(), self.window)
            polygon.setColor(self.color)
            polygon.setTexCoords(self.uv)
            polygon.setTexture(self.texture)
            polygon.drawPolygon(mode)
        
        if self.shader:
            GL.glUseProgram(0)

        if self.window:
            if self.window.debugmenu == 3:
                self.window.drawText(f"ID:{self.id}", self.position, debug_only=True)
