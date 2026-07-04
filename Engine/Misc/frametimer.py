from ..Kernel.kernel import classWrapper

@classWrapper
class frameTimer:
    def __init__(self, target_frame:int=0, func=None):
        self.frame = 0
        self.target = target_frame
        self.func = func
    
    def timerProcess(self):
        self.frame += 1
        
        if self.frame >= self.target:
            if self.func:
                self.func()
                self.frame = 0
            return True
        
        return False
