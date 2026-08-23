from ..Kernel.Kernel import log_system, LogWrapper
import os
import soundfile as sf

@LogWrapper
def AudioLoader(audio_path):
    log_system.AddInfo(f"Loading audio:{os.path.basename(audio_path)}")
    return sf.read(audio_path)
