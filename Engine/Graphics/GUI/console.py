from .imgui import GUIBegin, GUIInputTextMultiline, GUIBeginChild, GUIInputText, GUIButton, GUISameLine
from .imgui_flags import GUIFlags
from ..Window.console import consoleHandler
from ...Kernel.Components.vectors import Vec2
from ...Kernel.kernel import log_system

class Console:
    def __init__(self, console:consoleHandler):
        self.console = console
        self.text = ""
        log_system.addDInfo("Init GUI Console")

    def drawConsole(self):
        with GUIBegin("Console"):
            GUIInputTextMultiline("", self.console.output, size=Vec2(-1, -20), flags=GUIFlags.INPUT_TEXT_READ_ONLY)

            with GUIBeginChild("Bottom", border=False, size=Vec2(-1, 40)):
                _, self.text = GUIInputText("", self.text)
                GUISameLine()
                if GUIButton("Send", Vec2(-1, 0)) and self.text:
                    self.console.handleCommand(self.text)
                    self.text = ""
                