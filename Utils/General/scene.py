from ..System.manager import Manager
from ...Core.glob import log_system, classWrapper

@classWrapper
class sceneManager(Manager):
    def __init__(self):
        self.objs = []
        self.selected = None
        self.selected_inited = False
    
    def addScene(self, name:str, scene):
        index, s = self._find(name)
        if s:
            log_system.addError(f"Scene:{name} with this name already exists")
            return
        
        self.objs.append([name, scene])

    def removeScene(self, name:str):
        index, sound = self._find(name)
        if not sound:
            log_system.addError(f"Scene:{name} is not found!")
            return
        
        self.objs.remove(self.objs[index])
    
    def selectScene(self, name:str):
        if len(self.objs) == 0:
            log_system.addError("No scenes detected, create a scene.")
            return
        
        index, sound = self._find(name)
        if not sound:
            log_system.addError(f"Scene:{name} is not found!")
            return

        self.selected_inited = False
        self.selected = self.objs[index]

    def sceneProcess(self):
        if not self.selected:
            return
        
        if not self.selected_inited:
            if hasattr(self.selected[1], "sceneInit") and callable(self.selected[1].sceneInit):
                self.selected[1].sceneInit(self.selected[1])
            self.selected_inited = True
        
        if hasattr(self.selected[1], "sceneProcess") and callable(self.selected[1].sceneProcess):
            self.selected[1].sceneProcess(self.selected[1])
