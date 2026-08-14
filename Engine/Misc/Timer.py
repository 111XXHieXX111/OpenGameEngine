from ..Kernel.Kernel import ClassWrapper
import time

@ClassWrapper
class Timer:
    def __init__(self, target_sec:int, func=None):
        self.target = target_sec
        self.func = func
        self.last_trigger = time.time()
        self.triggered = False

    def Process(self):
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
