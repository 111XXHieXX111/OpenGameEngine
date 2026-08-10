from ...Kernel.kernel import render_items, log_system, classWrapper, textures2
from ...Misc.itemid import getItemByID
from ...Kernel.Components.graphics import Color4, textureType
from ...Kernel.Components.vectors import Vec2, Vec1
from ...Graphics.Utils.texture import loadTexture

@classWrapper
class consoleHandler:
    def __init__(self, window):
        self.output = ""
        self.helps = """Commands:
 help - open command list.
 clear - clear all output text.
 objlist - print all render objs.
 getfps - print fps.
 setcolor - set color for obj. Args:(id, R, G, B, A)
 setposition - set position for obj. Args:(id, X, Y)
 setrotation - set rotation for obj. Args:(id, R)
 setsize - set size for obj. Args:(id, X, Y)
 settex - set texture for obj. Args(id, tex_id)
 gettexs - print loaded textures.
 calcsize - calculate size for obj. Args(id)
 loadtexlin - load texture with linear type. Args(id, path)
 loadtexnear - load texture with nearest type. Args(id, path)
"""
        self.window = window
        log_system.addDInfo("Init console handler")

    def addOutput(self, text:str):
        self.output += f"{text}\n"

    def _operation_error(self, ex):
        self.addOutput("An error occurred while performing the operation")
        log_system.addDWarn(f"Console error:{ex}")

    def handleCommand(self, command:str):
        parts = command.split(" ")
        match parts[0]:
            case "help":
                for line in self.helps.splitlines():
                    self.addOutput(line)

            case "objlist":
                self.addOutput("Objects:")
                for item in render_items:
                    item_name = item.__class__.__name__
                    item_id = item.id
                    self.addOutput(f" {item_name}|{item_id}")

            case "clear":
                self.output = ""

            case "setcolor":
                try:
                    obj = getItemByID(int(parts[1]))
                    obj.color = Color4(
                        float(parts[2]), 
                        float(parts[3]), 
                        float(parts[4]),
                        float(parts[5])
                    )
                    self.addOutput("Successfully completed")
                except Exception as ex:
                    self._operation_error(ex)

            case "setposition":
                try:
                    obj = getItemByID(int(parts[1]))
                    obj.position = Vec2(
                        float(parts[2]), 
                        float(parts[3])
                    )
                    self.addOutput("Successfully completed")
                except Exception as ex:
                    self._operation_error(ex)

            case "setrotation":
                try:
                    obj = getItemByID(int(parts[1]))
                    obj.rotation = Vec1(
                        float(parts[2])
                    )
                    self.addOutput("Successfully completed")
                except Exception as ex:
                    self._operation_error(ex)
            
            case "setsize":
                try:
                    obj = getItemByID(int(parts[1]))
                    obj.size = Vec2(
                        float(parts[2]), 
                        float(parts[3])
                    )
                    self.addOutput("Successfully completed")
                except Exception as ex:
                    self._operation_error(ex)

            case "gettexs":
                try:
                    self.addOutput("Textures (Name, ID):")
                    for tex in textures2:
                        self.addOutput(f" {tex[0]} | {tex[1]}")
                except Exception as ex:
                    self._operation_error(ex)
                
            case "settex":
                try:
                    obj = getItemByID(int(parts[1]))
                    obj.texture = int(parts[2])
                    self.addOutput("Successfully completed")
                except Exception as ex:
                    self._operation_error(ex)

            case "calcsize":
                try:
                    obj = getItemByID(int(parts[1]))
                    obj.calculateSize()
                    self.addOutput("Successfully completed")
                except Exception as ex:
                    self._operation_error(ex)

            case "loadtexlin":
                try:
                    loadTexture(parts[1], textureType.LINEAR)
                    self.addOutput("Successfully completed")
                except Exception as ex:
                    self._operation_error(ex)

            case "loadtexnear":
                try:
                    loadTexture(parts[1], textureType.NEAREST)
                    self.addOutput("Successfully completed")
                except Exception as ex:
                    self._operation_error(ex)

            case "getfps":
                try:
                    self.addOutput(self.window.getFPS())
                except Exception as ex:
                    self._operation_error(ex)

            case _:
                self.addOutput(f"Command not found:{command}")
