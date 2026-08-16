from OpenGameEngine import *

window = Renderer.Window()

texture_raw = Renderer.TextureReader(textures.Get("Grid2")) 
texture = Renderer.TextureLoader(texture_raw, TextureFilter.NEAREST)

rect = gfx.Rectangle()
Transform.SetPosition(rect, Vec2(128, 128))
Transform.SetSize(rect, Vec2(256, 256))
Color.Set(rect, Color3(1, 1 ,1))
Texture.Set(rect, texture)
Texture.SetUV(rect, [Vec2(0, 0), Vec2(2, 0), Vec2(2, 2), Vec2(0, 2)])

@window.UpdateFunction
def Update():
    rect.Draw()

window.Run()