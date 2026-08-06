from ...Kernel.Components.vectors import Vec2
from ...Kernel.math import Math
from ..config import getGravity
from .Collider4 import collider4Body

class gravityBody:
    def __init__(self, autoconnect:bool=True, delta:bool=True):
        self.autoconnect = autoconnect
        self.delta = delta

    def _inited(self):
        self.current_body = None
        self.is_on_floor = False
        self.velocity = Vec2(0.0, 0.0)
        self.gravity = getGravity()
        self.max_velocity_y = 840.0
        self.connected_auto_connect = False
    
    def isOnFloor(self):
        return self.is_on_floor

    def setMaxVelocityY(self, velocity:int | float):
        self.max_velocity_y = velocity

    def _work(self, body):
        self.current_body = body

        if not self.connected_auto_connect and self.autoconnect:
            self.current_body.connectModule(collider4Body())
            self.connected_auto_connect = True

        self.is_on_floor = self.current_body.runModuleFunction("collider4Body", "getColliding", 2)
        
        if not self.is_on_floor:
            self.velocity.y += self.gravity
        else:
            if self.velocity.y >= 0:
                self.velocity.y = 0
        
        self.velocity.y = Math.Clamp(-(self.max_velocity_y*10), self.max_velocity_y, self.velocity.y)

        dt = 1.0
        if self.delta:
            dt = self.current_body.window.getDelta()

        self.velocity.x *= 0.5 ** dt

        self.current_body.position += self.velocity * dt
        self.current_body.calculateSize()
