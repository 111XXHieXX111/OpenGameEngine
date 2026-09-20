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
            current_time = time.perf_counter()
            self.fps = 1 / (current_time - self.prev_time) if self.prev_time else 0
            self.prev_time = current_time
        except ZeroDivisionError:
            return

@ClassWrapper
class DtFPSCounter:
    def __init__(self, window):
        self.prev_time = 0
        self.fps = 0
        self.window = window

    def FPSCalculate(self):
        try:
            self.fps = 1 / self.window.deltacounter.raw_delta
        except ZeroDivisionError:
            return

@ClassWrapper
class DeltaCounter:
    def __init__(self, window):
        self.prev_time = time.perf_counter()
        self.delta = 0
        self.raw_delta = 0
        self.window = window

    def DeltaCalculate(self):
        current_time = time.perf_counter()

        delta = current_time - self.prev_time
        self.delta, self.raw_delta = delta, delta

        self.prev_time = current_time

        if self.delta > 0.05:
            self.delta = 0.05
