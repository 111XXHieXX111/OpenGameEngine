from .Kernel import textures_path
from .Components.Graphical import TextureFilter
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

no_texture = None

def SetNoTexture():
    global no_texture

    if no_texture:
        return no_texture
    else:
        from ..Renderer.Textures.TextureReader import TextureReader
        from ..Renderer.Textures.TextureLoader import TextureLoader
        texture_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Textures", "notex.png")
        texture_raw = TextureReader(texture_path)
        texture = TextureLoader(texture_raw, TextureFilter.NEAREST)
        no_texture = texture
        return texture
