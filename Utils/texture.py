from ..Core.modules import Image, GL, np
from ..Core.base import textureType
from ..Core.glob import log_system

def loadTexture(path:str, textureType:textureType):
    log_system.addInfo(f"Loading texture {path}")

    img = Image.open(path).convert("RGBA")
    img_data = np.array(img, dtype=np.uint8)

    tex_id = GL.glGenTextures(1)
    GL.glBindTexture(GL.GL_TEXTURE_2D, tex_id)

    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_REPEAT)
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_REPEAT)
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, textureType)
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, textureType)

    GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGBA, img.width, img.height, 0, GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, img_data)

    GL.glBindTexture(GL.GL_TEXTURE_2D, 0)

    return tex_id
