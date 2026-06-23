from ...Core.base import Vec1, Vec2, Color3, Color4, drawMode, System
from ..objects.rectangle import Rectangle
from ...Core.modules import random
from ...Utils.frametimer import frameTimer

class Particle:
    def __init__(self, lifetime, gravity, color, size, position, particlelist):
        self.surface = Rectangle()
        self.surface.setColor(color)
        self.surface.setSize(size)
        self.surface.setPosition(position)
        
        self.gravity = gravity
        self.particlelist = particlelist
        
        self.lifetime_timer = frameTimer(lifetime, self.destroyParticle)
    
    def destroyParticle(self):
        self.particlelist.remove(self)
    
    def physicsProcess(self):
        self.surface.position.y += self.gravity.x
        self.surface.calculateSize()
        
        self.lifetime_timer.timerProcess()
        
    def drawParticle(self):
        self.surface.drawRectangle(drawMode.FILL)

class SimpleParticles:
    def __init__(self):
        self.position = Vec2(0.0, 0.0)
        self.gravity = Vec1(0.0)
        self.size = Vec2(0.0, 0.0)
        self.color = Color4(0.0, 0.0, 0.0, 0.0)
        self.spawnradius = Vec2(0.0, 0.0)
        self.lifetime = 0
        self.particles = []

    def setGravity(self, gravity:Vec1):
        self.gravity = gravity
    
    def setPosition(self, position:Vec2):
        self.position = position
    
    def setColor(self, color:Color3 | Color4):
        self.color = System.c3toc4(color, 1.0)
    
    def setSize(self, size:Vec2):
        self.size = size
    
    def setLifetime(self, frames:int=0):
        self.lifetime = frames
    
    def setSpawnRadius(self, radius:Vec2=Vec2(0.0, 0.0)):
        self.spawnradius = radius
    
    def addParticle(self):
        random_offset = Vec2(
            random.uniform(-self.spawnradius.x, self.spawnradius.x),
            random.uniform(-self.spawnradius.y, self.spawnradius.y)
        )
        self.particles.append(Particle(self.lifetime, self.gravity, self.color, self.size, self.position+random_offset, self.particles))
    
    def drawParticles(self):
        self.addParticle()
        
        for particle in self.particles:
            particle.physicsProcess()
            particle.drawParticle()