class SceneClass:
    def __init__(self):
        pass

    def SceneI(self):
        pass

    def SceneU(self):
        pass

class SceneManager:
    def __init__(self):
        self.scenes = []
        self.current_scene = None

    def AddScene(self, scene, name:str):
        self.scenes.append((scene, name))

    def SetScene(self, name:str):
        for scene in self.scenes:
            if scene[1] == name:
                self.current_scene = scene
                self.current_scene[0]()
                self.current_scene[0].SceneI(self.current_scene[0])

    def UnSetScene(self):
        self.current_scene = None

    def Process(self):
        if self.current_scene:
            self.current_scene[0].SceneU(self.current_scene[0])
