from ...Kernel.Kernel import log_system, LogWrapper
from PIL import Image
import os

@LogWrapper
def TextureReader(path:str):
    log_system.AddInfo(f"Reading texture:{os.path.basename(path)}")
    image = Image.open(path).convert("RGBA")
    return image
