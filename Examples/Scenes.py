from OpenGameEngine import *

window = Renderer.Window()

class Scene1(Misc.SceneClass):
    def SceneI(self):
        self.rect = gfx.Rectangle()
        Transform.SetPosition(self.rect, Vec2(20, 20))
        Transform.SetSize(self.rect, Vec2(80, 80))
        Color.Set(self.rect, Color3(0, 1, 0))
    
    def SceneU(self):
        self.rect.Draw()
    
class Scene2(Misc.SceneClass):
    def SceneI(self):
        self.rect = gfx.Rectangle()
        Transform.SetPosition(self.rect, Vec2(20, 20))
        Transform.SetSize(self.rect, Vec2(80, 80))
        Color.Set(self.rect, Color3(1, 0, 0))
    
    def SceneU(self):
        self.rect.Draw()
    
scenes = Misc.SceneManager()
scenes.AddScene(Scene1, "1")
scenes.AddScene(Scene2, "2")
scenes.SetScene("1")

@window.UpdateFunction
def Update():
    if Input.Keyboard.KeyJustPressed(Keys._1):
        scenes.SetScene("1")
    elif Input.Keyboard.KeyJustPressed(Keys._2):
        scenes.SetScene("2")
    
    scenes.Process()

window.Run()