from .sprite import Sprite
from ..Utils.texture import loadTexture
from ...Kernel.Components.graphics import textureType, Animation
from ...Kernel.kernel import log_system
from ...Misc.timer import Timer

class animatedSprite(Sprite):
    def __init__(self, window, updateFunction=None):
        super().__init__(window, self._update_function)
        self.window = window
        self.frames = []
        self.frame = 0
        self.animations = []
        self.animation = None
        self.animtimer = Timer(0, self._next_frame)
        self.user_update_function = updateFunction
        self.playing = False
        
    def loadFrame(self, path:str, textureType:textureType):
        self.frames.append([loadTexture(path, textureType), len(self.frames)])
    
    def loadFrames(self, texture_paths:list[str] | tuple[str], textureType:textureType):
        for tex in texture_paths:
            self.frames.append([loadTexture(tex, textureType), len(self.frames)])

    def setFrame(self, frameid:int):
        for frame in self.frames:
            if frame[1] == frameid:
                self.surface.setTexture(frame[0])
                break
        else:
            log_system.addError(f"Frame not found:{frameid}")

    def addAnimation(self, animation:Animation):
        self.animations.append(animation)
    
    def removeAnimation(self, name:str):
        for index, anim in enumerate(self.animations):
            if anim.name == name:
                self.animations.pop(index)
                break
        else:
            log_system.addError(f"Animation not found:{name}")
    
    def setAnimation(self, name:str):
        for index, anim in enumerate(self.animations):
            if anim.name == name:
                self.animation = anim
                self.animtimer.target = anim.interval
                break
        else:
            log_system.addError(f"Animation not found:{name}")
    
    def _next_frame(self):
        if self.playing:
           total_frames = len(self.animation.frames)
           if total_frames > 0:
                self.setFrame(self.animation.frames[self.frame % total_frames])
                self.frame += 1
                if self.frame >= total_frames:
                    if self.animation.loop:
                        self.frame = 0
                    else:
                        self.playing = False

    def playAnimation(self, fromstart:bool=True):
        self.playing = True
        if fromstart:
            self.frame = 0
    
    def stopAnimation(self):
        self.playing = False

    def _update_function(self):
        if self.animation:
            self.animtimer.timerProcess(self.window)

        if self.user_update_function:
            self.user_update_function()
