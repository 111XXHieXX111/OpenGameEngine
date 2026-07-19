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

kevent = Keyboard.KeyPressed

def update():
    if kevent(Key("w"), window):
        player.position.y -= 8
    elif kevent(Key("s"), window):
        player.position.y += 8
    
    if kevent(Key("a"), window):
        player.position.x -= 8
    elif kevent(Key("d"), window):
        player.position.x += 8
    
    player.calculateSize()
    player.drawRectangle(drawMode.FILL)

window.winProcess(update, 60)