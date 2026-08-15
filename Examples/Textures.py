from OpenGameEngine import *

window = Renderer.Window()

texture_raw = Renderer.TextureReader(textures.Get("LightGrid")) 
texture = Renderer.TextureLoader(texture_raw, TextureFilter.NEAREST)

rect = gfx.Rectangle()
Transform.SetPosition(rect, Vec2(0, 0))
Transform.SetSize(rect, Vec2(512, 512))
Color.Set(rect, Color3(1, 1 ,1))
Texture.Set(rect, texture)

@window.UpdateFunction
def Update():
    rect.Draw()

window.Run()