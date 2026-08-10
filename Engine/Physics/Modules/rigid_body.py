from ...Kernel.Components.vectors import Vec2
from ...Kernel.math import Math
from ..config import getGravity
from .collider4 import collider4Body

class rigidBodyBox:
    def __init__(self, autoconnect:bool=True):
        self.autoconnect = autoconnect

    def _inited(self):
        self.current_body = None
        self.connected_auto_connect = False
        self.velocity = Vec2(0.0, 0.0)
        self.gravity = getGravity()
        self.bounce = 1.0
        self.friction = 1.0
        self.mass = 1.0
        self.wind = 0.0

    def _work(self, body):
        self.current_body = body

        # CONNECT MODULE

        if not self.connected_auto_connect and self.autoconnect:
            self.current_body.connectModule(collider4Body())
            self.connected_auto_connect = True
        
        # DELTA

        dt = self.current_body.window.getDelta()

        # GRAVITY

        self.velocity.y += self.gravity * dt
        
        # REBOUND

        if self.current_body.rMF("collider4Body", "getColliding", 3):
            self.velocity.x = abs(self.velocity.x) * self.bounce
            self.velocity.y *= (1 - self.friction * self.mass * 0.01)

        if self.current_body.rMF("collider4Body", "getColliding", 4):
            self.velocity.x = -abs(self.velocity.x) * self.bounce
            self.velocity.y *= (1 - self.friction * self.mass * 0.01)
        
        if self.current_body.rMF("collider4Body", "getColliding", 1):
            self.velocity.y = abs(self.velocity.y) * self.bounce
            self.velocity.x *= (1 - self.friction * self.mass * 0.01)

        if self.current_body.rMF("collider4Body", "getColliding", 2):
            self.velocity.y = -abs(self.velocity.y) * self.bounce
            self.velocity.x *= (1 - self.friction * self.mass * 0.01)
        
        # WIND

        self.velocity.x += self.wind

        # VELOCITY

        self.current_body.Move(self.velocity * dt)
