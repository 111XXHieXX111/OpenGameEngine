from .Kernel import LogWrapper, textures, log_system, shaders
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

@LogWrapper
def ReleaseTextures():
    if len(textures):
        log_system.AddDInfo(f"Releasing {len(textures)} textures")
        for texture in textures:
            texture.release()
    else:
        log_system.AddDInfo("Not textures for release")

@LogWrapper
def ReleaseShaders():
    if len(shaders):
        log_system.AddDInfo(f"Releasing {len(shaders)} shaders")
        for shader in shaders:
            shader.release()
    else:
        log_system.AddDInfo("Not shaders for release")

@LogWrapper
def ReleaseVAOs(objects):
    if len(objects):
        log_system.AddDInfo(f"Releasing {len(objects)} vao + vbo")
        for _object in objects:
            if _object[0]:
                _object[0].release()
            if _object[1]:
                _object[1].release()
    else:
        log_system.AddDInfo("Not VAO's for release")
