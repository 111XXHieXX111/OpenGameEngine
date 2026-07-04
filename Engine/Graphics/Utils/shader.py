from ...Kernel.modules import json, GL, compileShader
from ...Kernel.kernel import logWrapper, log_system

class Shader:
    frag = None
    vert = None
    program = None

@logWrapper
def loadShader(path:str):
    import lzma
    import base64
    
    log_system.addInfo(f"Load shader:{path}")
    
    # READ FILE
    
    with open(path, "r") as f:
        data = json.load(f)
    
    # DECODE FILE
    
    frag_bytes = base64.b64decode(data["f"])
    vert_bytes = base64.b64decode(data["v"])
    
    # DECOMPRESS FILE
    
    frag_dec = lzma.decompress(frag_bytes).decode("utf-8")
    vert_dec = lzma.decompress(vert_bytes).decode("utf-8")
    
    # COMPILE SHADER
    
    frag_shader = compileShader(frag_dec, GL.GL_FRAGMENT_SHADER)
    vert_shader = compileShader(vert_dec, GL.GL_VERTEX_SHADER)
    
    # CHECK SHADERS
    
    if not GL.glGetShaderiv(frag_shader, GL.GL_COMPILE_STATUS):
        log = GL.glGetShaderInfoLog(frag_shader)
        log_system.addError(f"Fragment Error:{log}")
        return None
    
    if not GL.glGetShaderiv(vert_shader, GL.GL_COMPILE_STATUS):
        log = GL.glGetShaderInfoLog(vert_shader)
        log_system.addError(f"Vertex Error:{log}")
        return None
    
    # CREATE PROGRAM
    
    program = GL.glCreateProgram()
    
    GL.glAttachShader(program, vert_shader)
    GL.glAttachShader(program, frag_shader)
    
    # LINK
    
    GL.glLinkProgram(program)
    
    # CHECK LINK
    
    if not GL.glGetProgramiv(program, GL.GL_LINK_STATUS):
        log = GL.glGetProgramInfoLog(program)
        log_system.addError(f"Link Error:{log}")
        return None
    
    # DELETE SHADERS
    
    GL.glDeleteShader(vert_shader)
    GL.glDeleteShader(frag_shader)
    
    # RETURN SHADER
    
    shader = Shader()
    shader.frag = frag_shader
    shader.vert = vert_shader
    shader.program = program
    
    return shader
