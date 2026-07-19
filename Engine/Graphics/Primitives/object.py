from ...Kernel.modules import time

_counter = 0

class GFXObject:
    def __init__(self):
        global _counter
        self.id = _counter
        _counter += 1
        super().__init__()
