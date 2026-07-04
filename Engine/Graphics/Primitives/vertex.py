from ...Kernel.kernel import classWrapper
from ...Kernel.Components.system import System
from .modules import *

@classWrapper
class Vertex:
    def __init__(self):
        self.position = Vec2(0.0, 0.0)
        self.size = Vec1(0.1)
        self.width = Vec1(1.0)
        self.color = Color4(0.0, 0.0, 0.0, 0.0)
        self.texcoord = Vec2(0,0)
    
    def setTexCoord(self, uv: Vec2):
        self.texcoord = uv

    def setColor(self, color:Color3 | Color4):
        self.color = System.c3toc4(color)
    
    def setPosition(self, new_position:Vec2):
        self.position = new_position
    
    def setSize(self, new_size:Vec1):
        self.size = new_size
    
    def setWidth(self, new_size:Vec1):
        self.width = new_size
    
    def drawVertex(self, begin:bool, end:bool, mode:drawMode):
        if self.size.x < 0.01:
            return

        if begin:
            GL.glPointSize(self.size.x)
            GL.glLineWidth(self.width.x)
            GL.glBegin(mode)
        
        GL.glColor4f(self.color.r, self.color.g, self.color.b, self.color.a)
        GL.glTexCoord2f(self.texcoord.x, self.texcoord.y)
        GL.glVertex2f(self.position.x, self.position.y)

        if end:
            GL.glEnd()
