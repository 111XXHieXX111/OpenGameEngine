from ..objects.rectangle import Rectangle
from ..objects.triangle import Triangle
from ...Core.base import drawMode, batchDrawing
from ...Core.glob import render_items, logWrapper
from ...Core.modules import GL

class batchRender:
    def __init__(self, batchMode:batchDrawing):
        self.vertexes = []
        self.colors = []
        self.mode = drawMode.FILL
        self.batchmode = batchMode
        self.count = 0
    
    @logWrapper
    def setDrawMode(self, drawMode:drawMode):
        self.mode = drawMode
    
    @logWrapper
    def addPrimitive(self, primitive:Rectangle | Triangle):
        primitive.calculateSize()
        
        # COUNT VERTEXES
        
        if isinstance(primitive, Rectangle):
            verts = primitive.vertexes
            indices = [0, 1, 2, 0, 2, 3]
            for idx in indices:
                self.vertexes.append(verts[idx])
                self.colors.append(primitive.color)
            self.count += 1
        
        elif isinstance(primitive, Triangle):
            for v in primitive.vertexes:
                self.vertexes.append(v)
                self.colors.append(primitive.color)
            self.count += 1

    @logWrapper
    def renderPrimitives(self):
        if not self.vertexes:
            return
        
        # DRAW VERTEXES
        
        GL.glBegin(GL.GL_TRIANGLES)
        for i, v in enumerate(self.vertexes):
            c = self.colors[i]
            GL.glColor4f(c.r, c.g, c.b, c.a)
            GL.glVertex2f(v.x, v.y)
        GL.glEnd()
        
        # BATCH MODES
        
        if self.batchmode == batchDrawing.DYNAMIC:
            self.vertexes.clear()
            self.colors.clear()
            self.count = 0
        
        # ADD ELEMENT
        
        render_items.append(f"Batch:{self.count}")
