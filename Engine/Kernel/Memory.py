from .Kernel import LogWrapper
import psutil
import os

_process = psutil.Process(os.getpid())
_peak = 0

@LogWrapper
def GetMemoryLoad():
    global _peak

    mem = _process.memory_info()
    current = mem.rss / (1024 * 1024)
    
    if current > _peak:
        _peak = current

    return {
        "rss":mem.rss / (1024 * 1024), 
        "vms":current,
        "peak":_peak
    }
