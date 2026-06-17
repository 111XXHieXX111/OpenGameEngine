from ...Core.modules import GL
from .vertex import Vertex
from .modules import *

class Polygon:
    def __init__(self, vertexes:list[Vec2] | tuple[Vec2]):
        self.vertexes = vertexes
        self.widthlines = Vec1(0.0)
        self.color = Color4(0.0, 0.0, 0.0, 0.0)
        self.texcoords = [Vec2(0,0)] * len(vertexes)
        self.texture = None
    
    def setTexture(self, texture):
        self.texture = texture

    def setTexCoords(self, coords:list[Vec2] | tuple[Vec2]):
        self.texcoords = list(coords)

    def setColor(self, color:Color3 | Color4):
        self.color = System.c3toc4(color)
    
    def setWidthLines(self, width:Vec1):
        self.widthlines = width
    
    def drawPolygon(self, mode:drawMode):
        if self.texture:
            GL.glEnable(GL.GL_TEXTURE_2D)
            GL.glBindTexture(GL.GL_TEXTURE_2D, self.texture)
        else:
            GL.glDisable(GL.GL_TEXTURE_2D)

        for i, v in enumerate(self.vertexes):
            vertex = Vertex()
            vertex.setPosition(v)
            vertex.setSize(self.widthlines)
            vertex.setColor(self.color)
            vertex.setTexCoord(self.texcoords[i])

            begin, end = False, False

            if i == 0:
                begin = True
            elif i == len(self.vertexes) - 1:
                end = True
            
            vertex.drawVertex(begin, end, mode)
