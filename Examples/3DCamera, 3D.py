from OpenGameEngine import *

window = Renderer.Window()
camera = Renderer.Camera3D()
window.SetCamera(camera)
camera.position = Vec3(5, 2, 5)

rects3d = []

texture_raw = Renderer.TextureReader(textures.Get("LightGrid"))
texture = Renderer.TextureLoader(texture_raw, TextureFilter.NEAREST)

for x in range(10):
    for z in range(10):
        rect = gfx.Cube()
        Transform.SetSize(rect, Vec3(1, 1, 1))
        Transform.SetPosition(rect, Vec3(x, 0, z))
        Color.Set(rect, Color3(1, 1, 1))
        Texture.Set(rect, texture)
        rects3d.append(rect)

@window.UpdateFunction
def Update():
    for rect in rects3d:
        rect.Draw()
    
    dt = window.GetDelta()
    
    if Input.Keyboard.KeyPressed(Keys.A):
        camera.yaw -= 80 * dt
    elif Input.Keyboard.KeyPressed(Keys.D):
        camera.yaw += 80 * dt
    
    if Input.Keyboard.KeyPressed(Keys.W):
        camera.pitch += 80 * dt
    elif Input.Keyboard.KeyPressed(Keys.S):
        camera.pitch -= 80 * dt
    
    if Input.Keyboard.KeyPressed(Keys.Q):
        camera.fov -= 80 * dt
    elif Input.Keyboard.KeyPressed(Keys.E):
        camera.fov += 80 * dt
    
    if camera.yaw > 360:
        camera.yaw = 0
    elif camera.yaw < 0:
        camera.yaw = 360
    
    if camera.pitch < -85:
        camera.pitch = -85
    elif camera.pitch > 85:
        camera.pitch = 85

    if camera.fov < 10:
        camera.fov = 10
    elif camera.fov > 120:
        camera.fov = 120

window.Run()