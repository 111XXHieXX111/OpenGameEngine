from ..Kernel.modules import time
from ..Kernel.Components.graphics import tweenType
from ..Kernel.math import cos, PI

class Tween:
    def __init__(self, startpoint, endpoint, duration:int | float, callback, tween:tweenType):
        self.startpoint = startpoint
        self.endpoint = endpoint
        self.callback = callback
        self.starttime = time.time()
        self.progress = 0.0
        self.tween = tween
        self.duration = duration
        self.finished = False

    def tweenProcess(self):
        if self.finished:
            return

        elapsed = time.time() - self.starttime
        raw_progress = min(elapsed / self.duration, 1.0)
        
        value = 0
        if self.tween == tweenType.LINEAR:
            value = self.startpoint + (self.endpoint - self.startpoint) * raw_progress
            
        elif self.tween == tweenType.EASE_IN_OUT:
            eased_progress = -(cos(PI * raw_progress) - 1) / 2
            value = self.startpoint + (self.endpoint - self.startpoint) * eased_progress

        self.callback(value)
        
        if self.tween == tweenType.LINEAR:
            self.progress = min(elapsed / self.duration, 1.0)
        
            value = self.startpoint + (self.endpoint - self.startpoint) * self.progress
        elif self.tween == tweenType.EASE_IN_OUT:
            self.progress = -(cos(PI * self.progress) - 1) / 2
            
            value = self.startpoint + (self.endpoint - self.startpoint) * self.progress
        
        self.callback(value)

        if raw_progress >= 1.0:
            self.is_finished = True
