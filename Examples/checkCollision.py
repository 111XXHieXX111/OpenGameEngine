import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from OpenGameEngine import *

window = Window(0)
window.initWindow()
window.setTitle("Collision game")
window.setSize(640, 480)
window.setStretch(stretchType.EXPAND)
window.setBG(Color3(0, 0, 0))

collide = Graphics.Rectangle(window)
rect = Graphics.Rectangle(window)
rect.setPosition(Vec2(60, 60))
rect.setSize(Vec2(20, 20))
rect.setColor(Color3(1, 1, 1))

collide = Graphics.Rectangle(window)
collide.setPosition(Vec2(120, 60))
collide.setSize(Vec2(20, 20))
collide.setColor(Color3(1, 0, 0))

inv = False

def update():
    global inv
    
    rect.drawRectangle(drawMode.FILL)
    collide.drawRectangle(drawMode.LOOP)
    
    colliding = checkCollision(rect.vertexes, collide.vertexes)
    
    window.drawText(str(f"Colliding:{colliding}"), Vec2(0, 0), Color3(1, 0, 0))

    if inv:
        rect.position.x -= 2
    else:
        rect.position.x += 2
    
    if rect.position.x >= 180:
        inv = True
    elif rect.position.x <= 60:
        inv = False
    
    rect.calculateSize()

window.winProcess(update, 60)