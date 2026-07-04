from ...Kernel.modules import json, GL, compileShader
from ...Kernel.kernel import logWrapper, log_system

class Shader:
    frag = None
    vert = None
    program = None
    uniforms = []
    
    def _apply_uniforms(self):
        for uniform in self.uniforms:
            loc = GL.glGetUniformLocation(self.program, uniform[0])
            if loc == -1:
                return

            value = uniform[1]
            
            if isinstance(value, (int, float)):
                if isinstance(value, int):
                    GL.glUniform1i(loc, value)
                else:
                    GL.glUniform1f(loc, value)
            elif isinstance(value, (list, tuple)):
                if len(value) == 1:
                    GL.glUniform1f(loc, value[0])
                elif len(value) == 2:
                    GL.glUniform2f(loc, value[0], value[1])
                elif len(value) == 3:
                    GL.glUniform3f(loc, value[0], value[1], value[2])
                elif len(value) == 4:
                    GL.glUniform4f(loc, value[0], value[1], value[2], value[3])

@logWrapper
def loadShader(path:str, uniforms:list[list]=[]):
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
    shader.uniforms = uniforms
    
    return shader
