import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from OpenGameEngine import *

window = Window()
window.initWindow()
window.setTitle("Parents!")
window.setBG(Color3(0.1, 0.1, 0.1))

rect1 = gfx.Rectangle(window)
rect1.setPosition(Vec2(20, 20))
rect1.setSize(Vec2(60, 60))
rect1.setColor(Color3(1, 0, 0))

rect2 = gfx.Rectangle(window)
rect2.setPosition(Vec2(120, 20))
rect2.setSize(Vec2(60, 60))
rect2.setColor(Color3(0, 1, 0))

rect1.addChild("Child", rect2)

speed = 200

def update():
    rect1.drawRectangle(drawMode.FILL)
    rect2.drawRectangle(drawMode.FILL)
    
    dt = window.getDelta()
    
    if Keyboard.KeyPressed(Key("a"), window):
        rect1.Move(Vec2(-speed*dt, 0))
    elif Keyboard.KeyPressed(Key("d"), window):
        rect1.Move(Vec2(speed*dt, 0))
    
    if Keyboard.KeyPressed(Key("w"), window):
        rect1.Move(Vec2(0, -speed*dt))
    elif Keyboard.KeyPressed(Key("s"), window):
        rect1.Move(Vec2(0, speed*dt))
    
    if Keyboard.KeyPressed(Key("up"), window):
        rect1.reSize(Vec2(0.4, 0.4))
    elif Keyboard.KeyPressed(Key("down"), window):
        rect1.reSize(Vec2(-0.4, -0.4))
    
    if Keyboard.KeyPressed(Key("left"), window):
        rect1.Rotate(Vec1(-0.2))
    elif Keyboard.KeyPressed(Key("right"), window):
        rect1.Rotate(Vec1(0.2))

window.winProcess(update)