import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from OpenGameEngine import *

window = Window()
window.initWindow()

layers = layerSystem()
layers.addLayer("back")
layers.addLayer("main")
layers.addLayer("front")

rect1 = gfx.Rectangle(window)
rect1.setPosition(Vec2(240, 0))
rect1.setSize(Vec2(400, 260))
rect1.setColor(Color4(1, 0, 0, 0.5))

rect2 = gfx.Rectangle(window)
rect2.setPosition(Vec2(240, 240))
rect2.setSize(Vec2(400, 240))
rect2.setColor(Color4(0, 0, 1, 0.5))

def playerUpdate():
    dt = window.getDelta()
    speed = player.customData["Speed"]*dt
    
    if Keyboard.KeyPressed(Key("a"), window):
        player.surface.Move(Vec2(-speed, 0))
    elif Keyboard.KeyPressed(Key("d"), window):
        player.surface.Move(Vec2(speed, 0))
    
    if Keyboard.KeyPressed(Key("w"), window):
        player.surface.Move(Vec2(0, -speed))
    elif Keyboard.KeyPressed(Key("s"), window):
        player.surface.Move(Vec2(0, speed))

player = Sprite(window, playerUpdate)
player.setPosition(Vec2(20, 20))
player.setSize(Vec2(40, 40))
player.setColor(Color3(0, 1, 0))
player.customData.update({"Speed":280})

layers.addObject("back", rect1, drawMode.FILL)
layers.addObject("front", rect2, drawMode.FILL)
layers.addObject("main", player, drawMode.FILL)

def update():
    layers.renderLayers()
        
window.winProcess(update)