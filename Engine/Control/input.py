from .keyboard import Keyboard
from .mouse import Mouse
from ..Kernel.Components.control import Key, MouseButton, kEvent, mEvent

class inputManager:
    def __init__(self, window):
        self.active_events = 0
        self.window = window

    def kEvent(self, keyname:str, event:kEvent):
        if event == kEvent.Pres:
            self.active_events += 1
            return Keyboard.KeyPressed(Key(keyname), self.window)
        elif event == kEvent.justP:
            self.active_events += 1
            return Keyboard.KeyJustPressed(Key(keyname), self.window)

    def mEvent(self, button:MouseButton, event:mEvent):
        if event == mEvent.Pres:
            self.active_events += 1
            return Mouse.MouseKeyPressed(self.window, button)
        elif event == mEvent.Rel:
            self.active_events += 1
            return Mouse.MouseKeyReleased(self.window, button)
