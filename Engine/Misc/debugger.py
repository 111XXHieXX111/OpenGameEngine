from ..Kernel.Components.graphics import drawMode, Color4
from ..Kernel.Components.control import MouseButton
from ..Kernel.Components.vectors import Vec1, Vec2
from ..Control.mouse import Mouse
from ..Graphics.Primitives.arrow import Arrow
from ..Graphics.Primitives.circle import Circle

class Debugger:
    def __init__(self):
        self.drawmode = None
        self.showmouseclicks = True
        self.window = None
        self.mkp = Mouse.MouseKeyPressed
        self.mkr = Mouse.MouseKeyReleased
        self.firstclickpos = Vec2(0.0, 0.0)
        self.lastclickpos = Vec2(0.0, 0.0)

        self.was_pressed = False
        self.is_pressed = False

    def debugDraw(self, yes:bool):
        if yes:
            self.drawmode = drawMode.LOOP
        else:
            self.drawmode = None

    def showMouseClicks(self, show:bool):
        self.showmouseclicks = show

    def _debugger_connected(self, win):
        self.window = win
        self.clickarrow = Arrow(self.window)
        self.clickcircle1 = Circle(32, self.window)
        self.clickcircle2 = Circle(32, self.window)
        self.clickcircle3 = Circle(32, self.window)

        self.clickarrow.setColor(Color4(0.0, 1.0, 0.0, 0.5))
        self.clickarrow.setWidthLines(Vec1(2.0))
        self.clickcircle1.setColor(Color4(0.0, 0.0, 1.0, 0.5))
        self.clickcircle2.setColor(Color4(1.0, 0.0, 0.0, 0.5))
        self.clickcircle3.setColor(Color4(1.0, 1.0, 1.0, 0.5))
        self.clickcircle1.setSize(Vec2(20.0, 20.0))
        self.clickcircle2.setSize(Vec2(20.0, 20.0))
        self.clickcircle3.setSize(Vec2(20.0, 20.0))

    def _debugger_work(self):
        if self.showmouseclicks:
            mouse_pos = Mouse.getPosition(self.window)

            current_pressed = self.mkp(self.window, MouseButton.LEFT) or self.mkp(self.window, MouseButton.RIGHT) or self.mkp(self.window, MouseButton.MIDDLE)
            
            if current_pressed and not self.was_pressed:
                self.firstclickpos = mouse_pos
                self.is_pressed = True

            if not current_pressed and self.was_pressed:
                self.is_pressed = False
            
            self.was_pressed = current_pressed

            if self.is_pressed:
                self.clickarrow.setPoint1(self.firstclickpos)
                self.clickarrow.setPoint2(mouse_pos)
                self.clickarrow.drawArrow()
                self.lastclickpos = mouse_pos

            self.clickcircle1.setPosition(self.firstclickpos)
            self.clickcircle1.drawCircle(drawMode.FILL)

            self.clickcircle2.setPosition(self.lastclickpos)
            self.clickcircle2.drawCircle(drawMode.FILL)

            self.clickcircle3.setPosition(mouse_pos)
            self.clickcircle3.drawCircle(drawMode.FILL)
