from ..Kernel.modules import time
from ..Kernel.kernel import classWrapper

@classWrapper
class Timer:
    def __init__(self, target_sec:int=0, func=None):
        self.target = target_sec
        self.func = func
        self.last_trigger = time.time()
        self.triggered = False

    def timerProcess(self, window):
        current_time = time.time()
        
        if not self.triggered and current_time - self.last_trigger >= self.target:
            self.triggered = True
            if self.func:
                self.func()
            self.last_trigger = current_time
            return True
        
        if current_time - self.last_trigger < self.target:
            self.triggered = False
            
        return False