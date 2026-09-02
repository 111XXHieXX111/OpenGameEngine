from .Kernel import log_system, ClassWrapper

@ClassWrapper
class ConsoleHandler:
    def __init__(self):
        self.commands = """Commands:
help - this menu
"""
        self.output = []

        # For the future:
        #   t2SetPosition - set position for 2D obj. Args:(id, X, Y)
        #   t3SetPosition - set position for 3D obj. Args:(id, X, Y, Z)
        #   t2SetSize - set position for 2D obj. Args:(id, X, Y)
        #   t3SetSize - set position for 3D obj. Args:(id, X, Y, Z)
        #   SetColor3 - set color RGB for obj. Args:(id, R, G, B)
        #   SetColor4 - set color RGBA for obj. Args:(id, R, G, B, A)

    def GetOutput(self):
        return self.output

    def SendCommand(self, cmd:str):
        log_system.AddDInfo(f"Handling command: {cmd}")
        
        match cmd:
            case "help":
                self.output.append(self.commands)

            case _:
                log_system.AddDWarn(f"Command not found: {cmd}")
