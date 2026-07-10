import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from OpenGameEngine import *

window = Window()
window.initWindow()
window.setBG(Color3(0, 0.5, 0))
window.setTitle("Dragging")

rect = Graphics.Rectangle(window)
rect.setPosition(Vec2(20, 20))
rect.setSize(Vec2(40, 40))
rect.setColor(Color3(0, 0, 0))

mouserect = Graphics.Rectangle(window)
mouserect.setSize(Vec2(10, 10))

def update():
    mousePos = Mouse.getPosition(window)
    
    McenterX = mousePos.x - mouserect.size.x / 2
    McenterY = mousePos.y - mouserect.size.y / 2
    
    mouserect.setPosition(Vec2(McenterX, McenterY))
    mouserect.calculateSize()
    
    if Mouse.MouseKeyPressed(window, MouseButton.LEFT):
        if checkCollision(mouserect.vertexes, rect.vertexes):
            RcenterX = mouserect.position.x - rect.size.x / 2
            RcenterY = mouserect.position.y - rect.size.y / 2
            
            rect.setPosition(Vec2(RcenterX, RcenterY))
            rect.calculateSize()
    
    rect.drawRectangle(drawMode.FILL)

window.winProcess(update)