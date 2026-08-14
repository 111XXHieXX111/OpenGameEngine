from ....Kernel.Components.Vectors import Vec2
from ....Kernel.Memory import GetMemoryLoad
from ....Kernel.Kernel import render_items, LogWrapper
from ....Input.Mouse import _Mouse
from ....Misc.Timer import Timer
from ..imgui_flags import Flags
from ..imgui import Begin, Label, SameLine
import threading

@LogWrapper
class InfoMonitor:
    def __init__(self, window):
        self.rss = 0.0
        self.vms = 0.0
        self.peak = 0.0
        self.winsize = Vec2(0.0, 0.0)
        self.mousepos = Vec2(0.0, 0.0)
        self.threads = []
        self.render_objs = []
        self.fps = 0.0
        self.delta = 0.0

        self.window = window
        self.Timer = Timer(1, self._update_info)
    
    def _update_info(self):
        # Memory
        data = GetMemoryLoad()
        self.rss = data["rss"]
        self.vms = data["vms"]
        self.peak = data["peak"]

        del data

        # Window
        self.winsize = self.window.current_window_sizes
        self.mousepos = _Mouse.GetPosition()
        self.threads = threading.activeCount()
        self.render_objs = render_items
        self.fps = self.window.GetFPS()
        self.delta = self.window.GetDelta()

    def Render(self):
        self.Timer.Process()

        # Render
        with Begin("Memory", Vec2(20, 20), Vec2(320, 60), False, Flags.WINDOW_NO_MOVE | Flags.WINDOW_NO_RESIZE | Flags.WINDOW_NO_COLLAPSE):
            Label(f"RSS:{self.rss:.2f}MB")
            SameLine()
            Label(f"VMS:{self.vms:.2f}MB")
            SameLine()
            Label(f"PEAK:{self.peak:.2f}MB")

        with Begin("Window", Vec2(20, 100), Vec2(320, 140), False, Flags.WINDOW_NO_MOVE | Flags.WINDOW_NO_RESIZE | Flags.WINDOW_NO_COLLAPSE):
            Label(f"FPS:{self.fps:.2f}")
            Label(f"Delta:{self.delta:.8f}")
            Label(f"Window size:{int(self.winsize.x)}x{int(self.winsize.y)}")
            Label(f"Mouse position X:{int(self.mousepos.x)} Y:{int(self.mousepos.y)}")
            Label(f"Render objects:{len(self.render_objs)}")
            Label(f"Threads:{self.threads}")
