import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from OpenGameEngine import *

window = Window()
window.initWindow()

inputs = inputManager(window)

player = Graphics.Rectangle(window)
player.setPosition(Vec2(40, 40))
player.setSize(Vec2(80, 80))
player.setColor(Color3(1, 0, 0))
player.connectModule(gravityBody())

platform1 = Graphics.Rectangle(window)
platform1.setPosition(Vec2(0, 200))
platform1.setSize(Vec2(120, 80))
platform1.setColor(Color3(1, 1, 1))

platform2 = Graphics.Rectangle(window)
platform2.setPosition(Vec2(200, 250))
platform2.setSize(Vec2(120, 80))
platform2.setColor(Color3(1, 1, 1))

platform3 = Graphics.Rectangle(window)
platform3.setPosition(Vec2(400, 300))
platform3.setSize(Vec2(220, 80))
platform3.setColor(Color3(1, 1, 1))

def update():
    platform1.drawRectangle(drawMode.FILL)
    platform2.drawRectangle(drawMode.FILL)
    platform3.drawRectangle(drawMode.FILL)
    
    velocity = player.getModuleValue("gravityBody", "velocity")
    
    if inputs.kEvent("a", kEvent.Pres):
        velocity.x = -440
    elif inputs.kEvent("d", kEvent.Pres):
        velocity.x = 440
    else:
        velocity.x = 0
    
    if inputs.kEvent("space", kEvent.justP) and player.getModuleValue("gravityBody", "is_on_floor"):
        velocity.y -= 1800
        velocity.x *= 1.8
    
    player.setModuleValue("gravityBody", "velocity", velocity)
    
    player.drawRectangle(drawMode.FILL)

window.winProcess(update)