from .audio import loadSound
from ..Kernel.kernel import logWrapper, log_system
from ..Kernel.modules import os
from ..Kernel.Components.graphics import textureType
from ..Graphics.Utils.texture import loadTexture

@logWrapper
def loadResource(path:str, textureType:textureType=textureType.NEAREST, soundtype:str="float32"):
    filename = os.path.basename(path)
    log_system.addInfo(f"Load resource:{filename}")

    log_system.addDInfo("Read resource file")
    
    with open(path, "rb") as f:
        restype = f.readline().decode().strip()
        resfile = f.read()

    log_system.addDInfo(f"Resource type:{restype}")

    if restype == "Texture":
        with open("tmp.tmp", "wb+") as f:
            f.write(resfile)
        texture = loadTexture("tmp.tmp", textureType)
        if os.path.exists("tmp.tmp"):
            os.remove("tmp.tmp")
        return texture
    elif restype == "Sound":
        with open("tmp.tmp", "wb+") as f:
            f.write(resfile)
        sound = loadSound("tmp.tmp", soundtype)
        if os.path.exists("tmp.tmp"):
            os.remove("tmp.tmp")
        return sound
