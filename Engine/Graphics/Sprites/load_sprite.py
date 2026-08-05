from .sprite import Sprite
from ..Utils.texture import loadTexture
from ...Kernel.Components.graphics import textureType

class loadSprite(Sprite):
    def __init__(self, texture_path:str, texture_type:textureType, window=None, updateFunction=None):
        super().__init__(window, updateFunction)
        self.surface.setTexture(loadTexture(texture_path, texture_type))
