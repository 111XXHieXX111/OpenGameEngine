from OpenGameEngine import *

camera = Renderer.Camera2D()
window = Renderer.Window()
window.SetCamera(camera)
window.SetVSync(0)

rectangle = gfx.Rectangle()
    
Transform.SetPosition(rectangle, Vec2(5, 5))
Transform.SetSize(rectangle, Vec2(60, 60))

@window.UpdateFunction
def Update():
    if Input.Keyboard.KeyPressed(Keys.A):
        camera.position.x -= 1*window.GetDelta()
    if Input.Keyboard.KeyPressed(Keys.D):
        camera.position.x += 1*window.GetDelta()
    
    if Input.Keyboard.KeyPressed(Keys.W):
        camera.position.y -= 1*window.GetDelta()
    if Input.Keyboard.KeyPressed(Keys.S):
        camera.position.y += 1*window.GetDelta()
    
    if Input.Keyboard.KeyPressed(Keys.UP):
        camera.zoom += 1*window.GetDelta()
    if Input.Keyboard.KeyPressed(Keys.DOWN):
        camera.zoom -= 1*window.GetDelta()
    
    rectangle.Draw()

window.Run()