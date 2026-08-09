from .imgui import GUIBegin, GUIText, GUISameLine
from ...Kernel.Components.vectors import Vec2
from ...Kernel.kernel import render_items
from ...Kernel.modules import threading
from ...Control.mouse import Mouse
from ...Misc.timer import Timer
from .imgui_flags import GUIFlags

class infoMenu:
    def __init__(self, window):
        self.upd_timer = Timer(0.5, self.updInfo)
        self.window = window

        # MEMORY

        self.rss = 0
        self.vms = 0
        self.peak = 0

        self.fps = 0
        self.winsize = [0.0, 0.0]
        self.mousepos = Vec2(0.0, 0.0)
        self.render_objs = 0
        self.threads = 0
    
    def updInfo(self):
        
        # MEMORY

        data = self.window.memorymonitor.getMemory()
        self.rss = data["rss"]
        self.vms = data["vms"]
        self.peak = data["peak"]

        del data

        # WINDOW

        self.fps = self.window.fps
        self.winsize = self.window.current_window_sizes
        self.mousepos = Mouse.getPosition(self.window)
        self.render_objs = render_items
        self.threads = threading.active_count()
        self.delta = self.window.delta_time

    def infoMenuDraw(self):
        self.upd_timer.timerProcess(self.window)

        with GUIBegin("Memory", Vec2(20, 20), Vec2(320, 60), False, GUIFlags.WINDOW_NO_MOVE | GUIFlags.WINDOW_NO_RESIZE | GUIFlags.WINDOW_NO_COLLAPSE):
            GUIText(f"RSS:{self.rss:.2f}MB")
            GUISameLine()
            GUIText(f"VMS:{self.vms:.2f}MB")
            GUISameLine()
            GUIText(f"PEAK:{self.peak:.2f}MB")

        with GUIBegin("Window", Vec2(20, 100), Vec2(320, 140), False, GUIFlags.WINDOW_NO_MOVE | GUIFlags.WINDOW_NO_RESIZE | GUIFlags.WINDOW_NO_COLLAPSE):
            GUIText(f"FPS:{self.fps}")
            GUIText(f"Delta:{self.delta:.12f}")
            GUIText(f"Window size:{int(self.winsize[0])}x{int(self.winsize[1])}")
            GUIText(f"Mouse position:{int(self.mousepos.x)}x{int(self.mousepos.y)}")
            GUIText(f"Render objects:{len(self.render_objs)}")
            GUIText(f"Threads:{self.threads}")
