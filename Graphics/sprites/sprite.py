from ..objects.rectangle import Rectangle
from ...Core.base import Vec2, drawMode, Color3, Color4

class Sprite:
    def __init__(self, window=None, updateFunction=None):
        self.surface = Rectangle(window)
        self.updateFunction = None
        self.position = Vec2(0.0, 0.0)
        self.size = Vec2(0.0, 0.0)
        self.color = Color4(0.0, 0.0, 0.0, 0.0)
        self.updateFunction = updateFunction
        self.customData = {}
    
    def setPosition(self, new_position:Vec2):
        self.position = new_position
        self.surface.setPosition(self.position)
    
    def setSize(self, new_size:Vec2):
        self.size = new_size
        self.surface.setSize(new_size)
    
    def setColor(self, new_color:Color3 | Color4):
        self.color = new_color
        self.surface.setColor(self.color)
    
    def spriteProcess(self):
        if self.updateFunction:
            self.updateFunction()
        
        self.surface.calculateSize()
        self.surface.drawRectangle(drawMode.FILL)
