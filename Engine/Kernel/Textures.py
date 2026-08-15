from .Kernel import textures_path
import glob
import os

_textures = glob.glob(os.path.join(textures_path, "*.png"))

class Textures:
    def __init__(self):
        self.textures = []

    def Load(self):
        for tex in _textures:
            try:
                self.textures.append([os.path.basename(tex).split(".")[0], tex])
            except:...

    def Get(self, name:str):
        for tex in self.textures:
            if tex[0] == name:
                return tex[1]

textures = Textures()
textures.Load()
