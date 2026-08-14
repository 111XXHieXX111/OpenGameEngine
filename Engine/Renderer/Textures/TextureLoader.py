from ...Kernel.Kernel import log_system, LogWrapper, GetCurrentWindow
from ...Kernel.Components.Graphical import TextureFilter
from PIL import Image

@LogWrapper
def TextureLoader(raw_texture:Image, _filter:TextureFilter):
    window = GetCurrentWindow()

    context = window.window_renderer.context

    log_system.AddInfo("Creating texture")

    texture = context.texture(
        size=raw_texture.size,
        components=4,
        data=raw_texture.tobytes()
    )

    texture.filter = (_filter, _filter)

    return texture
