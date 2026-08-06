import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from OpenGameEngine import *

window = Window()
window.initWindow()

rect = gfx.Rectangle(window)
rect.setPosition(Vec2(40, 40))
rect.setSize(Vec2(40, 40))
rect.setColor(Color3(1, 1, 1))
rect.connectModule(collider4Body())

speed = 240

wall0 = gfx.Rectangle(window)
wall1 = gfx.Rectangle(window)
wall2 = gfx.Rectangle(window)
wall3 = gfx.Rectangle(window)

wall0.setPosition(Vec2(0, 0))
wall1.setPosition(Vec2(0, 0))
wall2.setPosition(Vec2(0, 480))
wall3.setPosition(Vec2(0, 480))

wall0.setSize(Vec2(20, 480))
wall1.setSize(Vec2(640, 20))
wall2.setSize(Vec2(640, 20))
wall3.setSize(Vec2(20, 480))

wall0.setColor(Color3(1, 1, 1))
wall1.setColor(Color3(1, 1, 1))
wall2.setColor(Color3(1, 1, 1))
wall3.setColor(Color3(1, 1, 1))

def update():
    dt = window.getDelta()
    dtspeed = dt*speed
    
    if Keyboard.KeyPressed(Key("a"), window):
        rect.position.x -= dtspeed
    elif Keyboard.KeyPressed(Key("d"), window):
        rect.position.x += dtspeed
    
    if Keyboard.KeyPressed(Key("w"), window):
        rect.position.y -= dtspeed
    elif Keyboard.KeyPressed(Key("s"), window):
        rect.position.y += dtspeed
    
    rect.calculateSize()
    
    wall0.drawRectangle(drawMode.FILL)
    wall1.drawRectangle(drawMode.FILL)
    wall2.drawRectangle(drawMode.FILL)
    wall3.drawRectangle(drawMode.FILL)
    
    rect.drawRectangle(drawMode.FILL)
    
    if rect.runModuleFunction("collider4Body", "getColliding", 1):
        rect.position.y += dtspeed
    if rect.runModuleFunction("collider4Body", "getColliding", 2):
        rect.position.y -= dtspeed
    if rect.runModuleFunction("collider4Body", "getColliding", 3):
        rect.position.x += dtspeed
    if rect.runModuleFunction("collider4Body", "getColliding", 4):
        rect.position.x -= dtspeed

window.winProcess(update)