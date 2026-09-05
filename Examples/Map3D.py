from OpenGameEngine import *

window = Renderer.Window(use_gl_im=False)

camera = Renderer.Camera3D()
window.SetCamera(camera)

map3d = Misc.Map3D("Resources/Test001.res")
Transform.SetPosition(map3d, Vec3(3, -1, 0))

@window.UpdateFunction
def update():
    map3d.Render()

window.Run()