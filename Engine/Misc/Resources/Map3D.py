from ...Kernel.Components.Vectors import Vec3
from ...Kernel.Components.Graphical import Color4
from ...Kernel.Kernel import ClassWrapper, log_system
from ...Primitives.Transform import Transform
from ...Primitives.Color import Color
from ...Primitives._3D.Cube import Cube
import json
import os

@ClassWrapper
class Map3D:
    def __init__(self, map3d_path:str):
        log_system.AddInfo(f"Loading Map3D:{os.path.basename(map3d_path)}")

        with open(map3d_path, "r") as f:
            data = json.load(f)
        
        self.objects = []

        readed_objs = 0

        for obj in data["Data"]["Objects"]:
            readed_objs += 1
            if obj[0] == 0:
                cube = Cube()
                Color.Set(cube, Color4(obj[11], obj[12], obj[13], obj[14]))
                self.objects.append([cube, Vec3(obj[2], obj[3], obj[4]), Vec3(obj[5], obj[6], obj[7]), Vec3(obj[8], obj[9], obj[10])])

        log_system.AddDInfo(f"Readed:{readed_objs} Objects")

        self.position = Vec3(0.0, 0.0, 0.0)
        self.rotation = Vec3(0.0, 0.0, 0.0)
        self.size = Vec3(1.0, 1.0, 1.0)

    def _build_model(self):
        pass

    def Render(self):
        for obj in self.objects:
            if isinstance(obj[0], Cube):
                obj[0].position = obj[1] + self.position
                obj[0].size = obj[2] * self.size
                obj[0].rotation = obj[3] + self.rotation
                obj[0]._build_model()

                obj[0].Draw()
