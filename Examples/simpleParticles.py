import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from OpenGameEngine import *

window = Window()
window.initWindow()
window.setBG(Color3(1, 1, 1))
window.setStretch(stretchType.EXPAND)

particles = Graphics.simpleParticles()
particles.setPosition(Vec2(100, 100))
particles.setColor(Color3(0.0, 0.0, 0.0))
particles.setSize(Vec2(20.0, 20.0))
particles.setGravity(Vec1(2.0))
particles.setSpawnRadius(Vec2(2.0, 2.0))
particles.setLifetime(60.0)
particles.setTexture(loadTexture(icons["Icon"], textureType.NEAREST))
particles.setDirectionX(Vec1(0.0))
particles.setRandomRotation(Vec1(0.0))
particles.setRandomSize(Vec2(5.0, 5.0), None)
particles.setRandomDirectionX(Vec2(-1.0, 1.0))
particles.setMaxParticles(1200)
particles.setRandomColor(True)

def update():
    if Keyboard.KeyPressed(Key("a"), window):
        particles.position.x -= 4
    elif Keyboard.KeyPressed(Key("d"), window):
        particles.position.x += 4
    
    if Keyboard.KeyPressed(Key("w"), window):
        particles.position.y -= 4
    elif Keyboard.KeyPressed(Key("s"), window):
        particles.position.y += 4
    
    particles.drawParticles()

window.winProcess(update, 60)