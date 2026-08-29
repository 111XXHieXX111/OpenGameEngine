from ..Kernel.Kernel import LogWrapper
from ..Kernel.Components.Graphical import TextureFilter
from ..Audio.AudioLoader import AudioLoader
from ..Renderer.Textures.TextureReader import TextureReader
from ..Renderer.Textures.TextureLoader import TextureLoader
import os
import glob

class ResourceType:
    TEXTURE_NEAREST = "TexN"
    TEXTURE_LINEAR = "TexL"
    AUDIO = "Audio"

@LogWrapper
def GetFilenameByPath(path:str):
    return os.path.basename(path).split(".")[0]

@LogWrapper
def LoadAudios(audios:list):
    _audios = {}

    for sound in audios:
        _audios.update({GetFilenameByPath(sound):AudioLoader(sound)})

    return _audios

@LogWrapper
def LoadTextures(textures:list, _textures_filter:TextureFilter):
    _textures ={}

    for texture in textures:
        texture_raw = TextureReader(texture)
        _textures.update({GetFilenameByPath(texture):TextureLoader(texture_raw, _textures_filter)})
        del texture_raw

    return _textures

@LogWrapper
def ResourceLoader(path:str, files:tuple[tuple[str, ResourceType]]):
    filespath = os.path.join(path, "")

    output = {}

    for file in files:
        _to_read_files = glob.glob(filespath + file[0])
        if file[1] == ResourceType.TEXTURE_NEAREST:
            _textures = LoadTextures(_to_read_files, TextureFilter.NEAREST)
            output.update(_textures)
        if file[1] == ResourceType.TEXTURE_LINEAR:
            _textures = LoadTextures(_to_read_files, TextureFilter.LINEAR)
            output.update(_textures)
        elif file[1] == ResourceType.AUDIO:
            _audios = LoadAudios(_to_read_files)
            output.update(_audios)

    return output
