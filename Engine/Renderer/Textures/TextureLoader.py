from ...Kernel.Kernel import log_system, LogWrapper, GetCurrentWindow, textures
from ...Kernel.Components.Graphical import TextureFilter
from PIL import Image

@LogWrapper
def TextureLoader(raw_texture:Image, _filter:TextureFilter):
    try:
        window = GetCurrentWindow()

        context = window.window_renderer.context

        log_system.AddInfo("Creating texture")

        texture = context.texture(
            size=raw_texture.size,
            components=4,
            data=raw_texture.tobytes()
        )

        texture.filter = (_filter, _filter)

        textures.append(texture)

        return texture
    except:
        from ...Kernel.Textures import SetNoTexture
        return SetNoTexture()
