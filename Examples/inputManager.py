import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from OpenGameEngine import *

window = Window(0)
window.initWindow()
window.setTitle("Example game")
window.setSize(640, 480)
window.setStretch(stretchType.KEEP_ASPECT)
window.setBG(Color3(0, 0.5, 0))

player = Graphics.Rectangle(window)
player.setPosition(Vec2(20, 20))
player.setSize(Vec2(60, 60))
player.setColor(Color3(0, 0, 0))

imanager = inputManager(window)

def update():
    if imanager.kEvent("w", kEvent.Pres):
        player.position.y -= 8
    if imanager.kEvent("s", kEvent.Pres):
        player.position.y += 8
    
    if imanager.kEvent("a", kEvent.Pres):
        player.position.x -= 8
    if imanager.kEvent("d", kEvent.Pres):
        player.position.x += 8
    
    player.calculateSize()
    player.drawRectangle(drawMode.FILL)

window.winProcess(update, 60)