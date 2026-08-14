from ...Kernel.Kernel import ClassWrapper
import time

@ClassWrapper
class FPSCounter:
    def __init__(self, window):
        self.prev_time = 0
        self.fps = 0
        self.window = window

    def FPSCalculate(self):
        try:
            current_time = time.time()
            self.fps = 1 / (current_time - self.prev_time) if self.prev_time else 0
            self.prev_time = current_time
        except ZeroDivisionError:
            return

@ClassWrapper
class DeltaCounter:
    def __init__(self, window):
        self.prev_time = time.time()
        self.delta = 0
        self.window = window

    def DeltaCalculate(self):
        current_time = time.time()
        self.delta = current_time - self.prev_time
        self.prev_time = current_time
        if self.delta > 0.05:
            self.delta = 0.05
