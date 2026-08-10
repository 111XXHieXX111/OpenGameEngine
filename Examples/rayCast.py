import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from OpenGameEngine import *

window = Window()
window.initWindow()

raycast = rayCast()
raycast.setPositions(Vec2(320, 0), Vec2(320, 480))

rect = gfx.Rectangle(window)
rect.setPosition(Vec2(20, 220))
rect.setSize(Vec2(40, 40))
rect.setColor(Color3(1, 0, 0))

rev = False

def update():
    global rev
    
    dt = window.getDelta()
    
    if rev:
        rect.Move(Vec2(-200*dt, 0))
    else:
        rect.Move(Vec2(200*dt, 0))
    
    if rect.position.x <= 20:
        rev = False
    elif rect.position.x >= 580:
        rev = True
    
    if raycast.colliding:
        rect.setColor(Color3(0, 1, 0))
    else:
        rect.setColor(Color3(1, 0, 0))
    
    rect.drawRectangle(drawMode.FILL)
    raycast.rayCastProcess()
    raycast.rayCastDraw()
    
window.winProcess(update)