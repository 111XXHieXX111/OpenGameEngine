from .imgui import GUIBegin, GUISameLine, GUIBeginChild, GUIInputText, GUIButton, GUIInputTextMultiline
from .imgui_flags import GUIFlags
from ..Window.console import consoleHandler
from ...Kernel.Components.vectors import Vec2
from ...Kernel.Components.control import Key
from ...Kernel.kernel import log_system
from ...Control.keyboard import Keyboard

class Console:
    def __init__(self, console:consoleHandler):
        self.console = console
        self.text = ""
        self.selected_memory = -1
        log_system.addDInfo("Init GUI Console")

    def drawConsole(self):
        with GUIBegin("Console"):
            GUIInputTextMultiline("", self.console.output, size=Vec2(-1, -20), flags=GUIFlags.INPUT_TEXT_READ_ONLY, buffer_length=-1)

            with GUIBeginChild("Bottom", border=False, size=Vec2(-1, 40)):
                _, self.text = GUIInputText("", self.text, buffer_length=-1)
                GUISameLine()
                if GUIButton("Send", Vec2(-1, 0)) and self.text:
                    self._send()
                
    def _send(self):
        self.console.handleCommand(self.text)
        self.text = ""

    def consoleProcess(self):
        if Keyboard.KeyJustPressed(Key("enter"), self.console.window):
            if self.text:
                self._send()
