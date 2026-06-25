from ...Core.modules import threading
from ...Core.glob import log_system
from ..System.manager import Manager

class loadSound:
    def __init__(self, path:str, audiotype:str="float32"):
        import soundfile as sf
        """audiotypes:float64, float32, int32, int16"""
        self.path = path
        self.audiotype = audiotype
        self._playing = False
        self._volume = 1.0
        self.data, self.fs = sf.read(self.path, dtype=self.audiotype)
        log_system.addInfo("Sound loaded")
    
    def play(self, loop:bool=False):
        import sounddevice as sd
        def _play():
            self._playing = True
            try:
                
                # CALCULATE VOLUME
                
                scaled_data = self.data * self._volume
                
                # CHECK LOOP
                
                if loop:
                    while self._playing:
                        sd.play(scaled_data, self.fs)
                        sd.wait()
                else:
                    sd.play(scaled_data, self.fs)
                    sd.wait()
            finally:
                self._playing = False
        
        # START THREADING
        
        threading.Thread(target=_play, daemon=True).start()

    def stop(self):
        import sounddevice as sd
        self._playing = False
        sd.stop()

    def isPlaying(self):
        return self._playing

    def getVolume(self):
        return self._volume

    def setVolume(self, volume:float):
        self._volume = volume

class soundManager(Manager):
    def __init__(self):
        self.objs = []

    def addSound(self, name:str, sound:loadSound):
        index, s = self._find(name)
        if s:
            log_system.addError(f"Sound:{name} with this name already exists")
            return
        
        self.objs.append([name, sound])
    
    def removeSound(self, name:str):
        index, sound = self._find(name)
        if not sound:
            log_system.addError(f"Sound:{name} is not found!")
            return
        
        self.objs.remove(self.objs[index])
    
    def playSound(self, name:str, loop:bool=False):
        index, sound = self._find(name)
        if not sound:
            log_system.addError(f"Sound:{name} is not found!")
            return

        sound.play(loop)
    
    def stopSound(self, name:str):
        index, sound = self._find(name)
        if not sound:
            log_system.addError(f"Sound:{name} is not found!")
            return

        sound.stop()
    
    def isPlayingSound(self, name:str):
        index, sound = self._find(name)
        if not sound:
            log_system.addError(f"Sound:{name} is not found!")
            return
        
        return sound.isPlaying()
    
    def setSoundVolume(self, name:str, volume:float):
        index, sound = self._find(name)
        if not sound:
            log_system.addError(f"Sound:{name} is not found!")
            return
        
        sound.setVolume(volume)
    
    def getSoundVolume(self, name):
        index, sound = self._find(name)
        if not sound:
            log_system.addError(f"Sound:{name} is not found!")
            return
        
        return sound.getVolume()
    
    def setGeneralVolume(self, volume:float):
        for sound in self.objs:
            sound[1].setVolume(volume)
    
    def stopSounds(self):
        for sound in self.objs:
            sound[1].stop()

    def getSound(self, name):
        index, sound = self._find(name)
        if not sound:
            log_system.addError(f"Sound:{name} is not found!")
            return

        return sound
