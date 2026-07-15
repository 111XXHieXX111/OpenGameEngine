from ...Kernel.kernel import render_items

class consoleHandler:
    def __init__(self, window):
        self.output = ""
        self.helps = """Commands:
 help - open command list
 objlist - print all render objs
 getfps - print fps"""
        self.window = window

    def addOutput(self, test:str):
        self.output += f"{test}\n"

    def handleCommand(self, command:str):
        match command:
            case "help":
                self.addOutput(self.helps)

            case "objlist":
                for item in render_items:
                    self.addOutput(item)

            case "getfps":
                self.addOutput(self.window.getFPS())

            case _:
                self.addOutput(f"Command not found:{command}")
