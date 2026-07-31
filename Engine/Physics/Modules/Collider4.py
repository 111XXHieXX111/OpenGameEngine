from ...Graphics.Primitives.rectangle import Rectangle
from ...Kernel.Components.graphics import drawMode, Color4
from ...Kernel.Components.vectors import Vec2
from ..Collision.Globals.aabb import _GAABB

class collider4Body:
    def __init__(self):
        pass

    def _inited(self):
        self.showcolliders = False
        self.colliders = []
        self.current_body = None

        self.top = Rectangle(self.window)
        self.bottom = Rectangle(self.window)
        self.left = Rectangle(self.window)
        self.right = Rectangle(self.window)

        self.colliders.append(self.top)
        self.colliders.append(self.bottom)
        self.colliders.append(self.left)
        self.colliders.append(self.right)

        self.top.setColor(Color4(0.0, 1.0, 1.0, 0.8))
        self.bottom.setColor(Color4(0.0, 1.0, 1.0, 0.8))
        self.left.setColor(Color4(0.0, 1.0, 1.0, 0.8))
        self.right.setColor(Color4(0.0, 1.0, 1.0, 0.8))
        
    def getColliding(self, collider:int):
        """Collider: 1 - top, 2 - bottom, 3 - left, 4 - right"""
        if self.current_body:
            return _GAABB(self.colliders[collider-1], [self.current_body] + self.colliders)
        else:
            return False

    def _work(self, body):
        self.current_body = body

        self.top.setPosition(Vec2(body.position.x, body.position.y-1))
        self.top.setSize(Vec2(body.size.x, 1))
        self.top.calculateSize()

        self.bottom.setPosition(Vec2(body.position.x, body.position.y+body.size.y))
        self.bottom.setSize(Vec2(body.size.x, 1))
        self.bottom.calculateSize()

        self.left.setPosition(Vec2(body.position.x-1, body.position.y))
        self.left.setSize(Vec2(1, body.size.y))
        self.left.calculateSize()

        self.right.setPosition(Vec2(body.position.x+body.size.x, body.position.y))
        self.right.setSize(Vec2(1, body.size.y))
        self.right.calculateSize()
    
        if self.showcolliders:
            self.top.drawRectangle(drawMode.FILL)
            self.bottom.drawRectangle(drawMode.FILL)
            self.left.drawRectangle(drawMode.FILL)
            self.right.drawRectangle(drawMode.FILL)
