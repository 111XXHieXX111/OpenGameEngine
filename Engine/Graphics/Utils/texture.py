from ...Kernel.modules import GL, os
from ...Kernel.Components.graphics import textureType
from ...Kernel.kernel import log_system, textures, logWrapper, textures2

@logWrapper
def loadTexture(path:str, textureType:textureType):
    
    tex_name = os.path.basename(path)

    log_system.addInfo(f"Load texture:{tex_name}")
    
    # IMPORT PILLOW
    
    from PIL import Image

    # READ TEXTURE

    log_system.addDInfo("Read texture file")

    img = Image.open(path).convert("RGBA")
    img_data = img.tobytes()

    # LOAD TEXTURE

    log_system.addDInfo("Load texture in OpenGL")

    tex_id = GL.glGenTextures(1)
    GL.glBindTexture(GL.GL_TEXTURE_2D, tex_id)

    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_REPEAT)
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_REPEAT)
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, textureType)
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, textureType)

    GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGBA, img.width, img.height, 0, GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, img_data)

    GL.glBindTexture(GL.GL_TEXTURE_2D, 0)
    
    textures.append(tex_id)
    textures2.append([tex_name, tex_id])
    
    return tex_id
