from ...Kernel.Kernel import log_system, LogWrapper
import os

@LogWrapper
def ShaderReader(*args:str):
    readed_shaders = []
    
    log_system.AddInfo(f"Reading {len(args)} shader files")

    for shader_path in args:
        try:
            with open(f"{shader_path}", "r") as f:
                readed_shaders.append(f.read())
                log_system.AddDInfo(f"Reading:{os.path.basename(shader_path)}")
        except Exception as ex:
            log_system.AddWarn(f"Shader reading error:{ex}")
            return []
            
    return readed_shaders
