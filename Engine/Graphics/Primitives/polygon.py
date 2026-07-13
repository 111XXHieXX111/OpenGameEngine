from ...Kernel.modules import GL, ctypes
from ...Kernel.kernel import classWrapper, getShader
from ...Kernel.Components.system import System
from .vertex import Vertex
from .modules import *

@classWrapper
class PolygonLegacy:
    def __init__(self, vertexes:list[Vec2] | tuple[Vec2]):
        self.vertexes = vertexes
        self.widthlines = Vec1(0.0)
        self.color = Color4(0.0, 0.0, 0.0, 0.0)
        self.texcoords = [Vec2(0,0)] * len(vertexes)
        self.pointsize = Vec1(1.0)
        self.texture = None
    
    def setTexture(self, texture):
        self.texture = texture

    def setTexCoords(self, coords:list[Vec2] | tuple[Vec2]):
        self.texcoords = list(coords)

    def setColor(self, color:Color3 | Color4):
        self.color = System.c3toc4(color)
    
    def setWidthLines(self, width:Vec1):
        self.widthlines = width
    
    def setPointSize(self, new_size:Vec1):
        self.pointsize = new_size
    
    def drawPolygon(self, mode:drawMode):
        if self.texture:
            GL.glEnable(GL.GL_TEXTURE_2D)
            GL.glBindTexture(GL.GL_TEXTURE_2D, self.texture)
        else:
            GL.glDisable(GL.GL_TEXTURE_2D)

        for i, v in enumerate(self.vertexes):
            vertex = Vertex()
            vertex.setPosition(v)
            vertex.setWidth(self.widthlines)
            vertex.setSize(self.pointsize)
            vertex.setColor(self.color)
            vertex.setTexCoord(self.texcoords[i])

            begin, end = False, False

            if i == 0:
                begin = True
            elif i == len(self.vertexes) - 1:
                end = True
            
            vertex.drawVertex(begin, end, mode)

class Polygon:
    def __init__(self, vertexes, window=None):
        self.vertexes = vertexes
        self.color = Color4(0.0, 0.0, 0.0, 0.0)
        self.texcoords = [Vec2(0,0)] * len(vertexes)
        self.texture = None
        self.window = window
        self._vao = None
        self._vbo = None
        self._dirty = True

    def setTexture(self, texture):
        self.texture = texture

    def setTexCoords(self, coords:list[Vec2] | tuple[Vec2]):
        self.texcoords = list(coords)

    def setColor(self, color:Color3 | Color4):
        self.color = System.c3toc4(color)

    def drawPolygon(self, mode:drawMode):
        if self._dirty:
            if isinstance(self.vertexes, list):
            
                # CONVERT LIST VEC2S TO ARRAY
            
                varray = []
                for index, v in enumerate(self.vertexes):
                
                    # CONVERT VEC2S VALUES FROM NDC TO PIXELS
                
                    nv = v
                    if self.window:
                        nv = System.pxtondc(v, self.window)

                    uv = self.texcoords[index]
                
                    varray.append(nv.x)
                    varray.append(nv.y)
                    varray.append(0.0)
                    varray.append(self.color.r)
                    varray.append(self.color.g)
                    varray.append(self.color.b)
                    varray.append(uv.x)
                    varray.append(uv.y)

                self.vertexes = System.arraytocarrayf(varray)

            self._vao = GL.glGenVertexArrays(1)
            GL.glBindVertexArray(self._vao)

            self._vbo = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self._vbo)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(self.vertexes) * 4, self.vertexes, GL.GL_STATIC_DRAW)

            stride = 8 * 4

            GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, stride, ctypes.c_void_p(0))
            GL.glEnableVertexAttribArray(0)

            GL.glVertexAttribPointer(1, 3, GL.GL_FLOAT, GL.GL_FALSE, stride, ctypes.c_void_p(12))
            GL.glEnableVertexAttribArray(1)

            GL.glVertexAttribPointer(2, 2, GL.GL_FLOAT, GL.GL_FALSE, stride, ctypes.c_void_p(24))
            GL.glEnableVertexAttribArray(2)

            self._dirty = False

        shader = getShader()

        GL.glUseProgram(shader)

        GL.glActiveTexture(GL.GL_TEXTURE0)

        if self.texture:
            GL.glEnable(GL.GL_TEXTURE_2D)
            GL.glBindTexture(GL.GL_TEXTURE_2D, self.texture)
        else:
            GL.glDisable(GL.GL_TEXTURE_2D)

        useTexture_loc = GL.glGetUniformLocation(shader, "useTexture")
        texture_loc = GL.glGetUniformLocation(shader, "textureSampler")

        if self.texture:
            GL.glUniform1i(useTexture_loc, 1)
            GL.glUniform1i(texture_loc, 0)
        else:
            GL.glUniform1i(useTexture_loc, 0)

        GL.glBindVertexArray(self._vao)
      
        GL.glDrawArrays(mode, 0, len(self.vertexes) // 8)
