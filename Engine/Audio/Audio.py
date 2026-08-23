import sounddevice as sd
import threading

class Audio:
    def __init__(self):
        self.source = None
        self.position = 0.0
        self.is_playing = False

    def SetSource(self, source:tuple):
        self.source = source
        
    def Play(self):
        if self.is_playing:
            return

        audio, rate = self.source
        start = int(self.position * len(audio))
        
        threading.Thread(target=self._play, args=(audio[start:], rate), daemon=True).start()
        self.is_playing = True

    def SetPosition(self, position:float):
        self.position = max(0.0, min(1.0, position))
        if self.is_playing:
            sd.stop()
            self.is_playing = False
            self.Play()

    def Stop(self):
        sd.stop()
        self.is_playing = False

    def _play(self, data, rate):
        sd.play(data, rate)
        sd.wait()
        self.is_playing = False

    @property
    def IsPlaying(self):
        return self.is_playing
