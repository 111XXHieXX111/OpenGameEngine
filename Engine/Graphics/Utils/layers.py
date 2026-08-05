from ...Kernel.Components.graphics import drawMode
from ...Kernel.kernel import log_system, classWrapper
from ..Primitives.rectangle import Rectangle
from ..Primitives.triangle import Triangle
from ..Primitives.circle import Circle
from ..Primitives.line import Line
from ..Primitives.polygon import Polygon, PolygonLegacy
from ..Primitives.arrow import Arrow
from ..Sprites.sprite import Sprite
from ..Sprites.animated_sprite import animatedSprite

@classWrapper
class layerSystem():
    def __init__(self):
        self.layers = {}

    def addLayer(self, layer_name:str):
        if layer_name in self.layers:
            log_system.addError(f"Layer:{layer_name} with this name already exists")
            return
        self.layers.update({f"{layer_name}":[]})

    def addObject(self, layer_name:str, obj:Rectangle | Triangle | Circle | Line | Polygon | PolygonLegacy | Arrow | Sprite| animatedSprite, mode:drawMode | None):
        if layer_name in self.layers:
            if [obj, mode] in self.layers[layer_name]:
                log_system.addError("The object is already there")
                return
            self.layers[layer_name].append([obj, mode])
            return
        log_system.addError(f"Layer:{layer_name} is not found!")

    def removeObject(self, layer_name:str, obj:Rectangle | Triangle | Circle | Line | Polygon | PolygonLegacy | Arrow | Sprite| animatedSprite, mode:drawMode | None):
        if layer_name in self.layers:
            if [obj, mode] in self.layers[layer_name]:
                self.layers[layer_name].remove([obj, mode])
                return
            log_system.addError("Object is not found!")
            return
        log_system.addError(f"Layer:{layer_name} is not found!")

    def removeLayer(self, layer_name:str):
        if layer_name in self.layers:
            self.layers.pop(layer_name)
            return
        log_system.addError(f"Layer:{layer_name} is not found!")

    def renderLayers(self):
        for objects in self.layers.values():
            for obj in objects:
                if isinstance(obj[0], Rectangle):
                    obj[0].drawRectangle(obj[1])
                elif isinstance(obj[0], Triangle):
                    obj[0].drawTriangle(obj[1])
                elif isinstance(obj[0], Circle):
                    obj[0].drawCircle(obj[1])
                elif isinstance(obj[0], Line):
                    obj[0].drawLine()
                elif isinstance(obj[0], (Polygon, PolygonLegacy)):
                    obj[0].drawPolygon(obj[1])
                elif isinstance(obj[0], Arrow):
                    obj[0].drawArrow()
                elif isinstance(obj[0], (Sprite, animatedSprite)):
                    obj[0].spriteProcess()
