from OpenGameEngine import *

window = Renderer.Window()
camera = Renderer.Camera2D()
window.SetCamera(camera)

@window.UpdateFunction
def update():
    GL_IM.glBegin()
    GL_IM.glColor3f(1, 0, 0)
    GL_IM.glVertex2f(20, 20)
    GL_IM.glColor3f(0, 1, 0)
    GL_IM.glVertex2f(200, 200)
    GL_IM.glColor3f(0, 0, 1)
    GL_IM.glVertex2f(120, 400)
    GL_IM.glEnd()

window.Run()