from ...Core.base import Vec1, Vec2, Color3, Color4, drawMode, System
from ...Core.modules import random
from ...Core.glob import classWrapper
from ...Utils.general.frametimer import frameTimer
from ..objects.rectangle import Rectangle
from .randomcolor import randomColor4

@classWrapper
class Particle:
    def __init__(self, window, lifetime, gravity, color, size, position, particlelist, texture, rotation, direction):
        self.surface = Rectangle(window)
        self.surface.setColor(color)
        self.surface.setSize(size)
        self.surface.setPosition(position)
        self.surface.setTexture(texture)
        self.surface.setRotation(rotation)
        
        self.gravity = gravity
        self.direction = direction
        self.particlelist = particlelist
        
        self.lifetime_timer = frameTimer(lifetime, self.destroyParticle)
    
    def destroyParticle(self):
        self.particlelist.remove(self)
    
    def physicsProcess(self):
        self.surface.position.y += self.gravity.x
        self.surface.position.x += self.direction.x
        self.surface.calculateSize()
        
        self.lifetime_timer.timerProcess()
        
    def drawParticle(self):
        self.surface.drawRectangle(drawMode.FILL)

@classWrapper
class simpleParticles:
    def __init__(self, window=None):
        
        # PARTICLES DATA
        
        self.particles = []
        self.max_particles = 120
        
        # SIZE
        
        self.size = Vec2(0.0, 0.0)
        self.rnd_size = Vec2(0.0, 0.0)
        self.rnd_size_rounded = True
        
        # POSITION
        
        self.position = Vec2(0.0, 0.0)
        self.spawnradius = Vec2(0.0, 0.0)
        
        # ROTATION
        
        self.rotation = Vec1(0.0)
        self.rnd_rotation = Vec1(0.0)
        
        # COLOR
        
        self.color = Color4(0.0, 0.0, 0.0, 0.0)
        self.rnd_color = False
        
        # TEXTURE
        
        self.texture = None
        
        # PHYSICS
        
        self.gravity = Vec1(0.0)
        
        # PROCESS
        
        self.lifetime = 0
        
        # DIRECTION
        
        self.directionX = Vec1(0.0)
        self.rnd_directionX = Vec2(0.0, 0.0)
        
        # WINDOW
        
        self.window = window

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
    
    def setTexture(self, texture):
        self.texture = texture
    
    def setDirectionX(self, dirX:Vec1):
        self.directionX = dirX
    
    def setRandomRotation(self, maxR:Vec1):
        self.rnd_rotation = maxR
    
    def setRandomSize(self, maxS:Vec2, rounded:bool=True):
        self.rnd_size = maxS
        self.rnd_size_rounded = rounded
    
    def setRandomDirectionX(self, maxD:Vec2):
        self.rnd_directionX = maxD
    
    def setRandomColor(self, enabled:bool):
        self.rnd_color = enabled
    
    def setMaxParticles(self, maxP:int):
        self.max_particles = maxP
    
    def clearParticles(self):
        self.particles.clear()
    
    def addParticle(self):
        
        # CHECK MAX PARTICLES
        
        if len(self.particles) > self.max_particles:
            
            # SKIP ADD
            
            return
        
        # GENERATE OFFSETS
        
        random_offset = Vec2(
            random.uniform(-self.spawnradius.x, self.spawnradius.x),
            random.uniform(-self.spawnradius.y, self.spawnradius.y)
        )
        
        if self.rnd_rotation:
            random_rotate = Vec1(
                random.uniform(0, self.rnd_rotation.x)
            )
        
        if self.rnd_size_rounded:
            size = random.uniform(-self.rnd_size.x, self.rnd_size.x)
            random_size = Vec2(size, size)
        else:
            random_size = Vec2(
                random.uniform(-self.rnd_size.x, self.rnd_size.x),
                random.uniform(-self.rnd_size.y, self.rnd_size.y)
            )

        if self.rnd_directionX:
            random_directionX = Vec1(
                random.uniform(self.rnd_directionX.x, self.rnd_directionX.y)
            )
        else:
            random_directionX = Vec1(0.0)
        
        if self.rnd_color:
            random_color = randomColor4(False)
        else:
            random_color = self.color
        
        # ADD PARTICLE
        
        self.particles.append(
            Particle(
                self.window,
                self.lifetime, 
                self.gravity, 
                random_color, 
                self.size+random_size,
                self.position+random_offset, 
                self.particles,
                self.texture,
                self.rotation+random_rotate,
                self.directionX+random_directionX
            )
        )
    
    def drawParticles(self):
        self.addParticle()
        
        for particle in self.particles:
            particle.physicsProcess()
            particle.drawParticle()
