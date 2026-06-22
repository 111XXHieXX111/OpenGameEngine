from ..Core.glob import debug
import os

class MemoryMonitor:
    def __init__(self):
        self.peak_memory = 0
        if debug:
            import psutil
            self.process = psutil.Process(os.getpid())
    
    def getMemory(self):
        if not hasattr(self, "process"):
            return {"rss": 0, "vms": 0, "peak": 0}
        
        mem = self.process.memory_info()
        current = mem.rss / (1024 * 1024)
        
        if current > self.peak_memory:
            self.peak_memory = current
        
        return {
            "rss": current,
            "vms": mem.vms / (1024 * 1024),
            "peak": self.peak_memory
        }