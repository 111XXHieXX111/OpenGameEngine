from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showerror
import lzma
import json
import base64
import threading

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

class App:
    def __init__(self, master:Tk):
        self.root = master
        
        self.winSettings()
        
        self.current_file = ""
        
        self.topframe = LabelFrame(self.root, text="Tools")
        self.topframe.pack(side="top", padx=5, pady=2, fill="x")
        
        self.bottomframe = Frame(self.root)
        self.bottomframe.pack(side="bottom", padx=5, pady=2, fill="both", expand=True)
        
        self.topbuttons = [
            Button(self.topframe, text="Open", command=self.open), 
            Button(self.topframe, text="Save", command=self.save), 
            Button(self.topframe, text="New", command=self.new)
        ]
        
        for btn in self.topbuttons:
            btn.pack(side="left", padx=2, pady=2)
        
        self.bottomframe.grid_rowconfigure(0, weight=0)
        self.bottomframe.grid_rowconfigure(1, weight=1)
        self.bottomframe.grid_rowconfigure(2, weight=0)
        self.bottomframe.grid_rowconfigure(3, weight=1)
        self.bottomframe.grid_columnconfigure(0, weight=1)
        
        self.labelfrag = Label(self.bottomframe, text="Fragment", anchor="w")
        self.labelfrag.grid(row=0, column=0, padx=5, pady=(5,0), sticky="ew")
        
        self.frageditor = Text(self.bottomframe)
        self.frageditor.grid(row=1, column=0, padx=5, pady=(0,5), sticky="nsew")
        
        self.labelvert = Label(self.bottomframe, text="Vertex", anchor="w")
        self.labelvert.grid(row=2, column=0, padx=5, pady=(5,0), sticky="ew")
        
        self.verteditor = Text(self.bottomframe)
        self.verteditor.grid(row=3, column=0, padx=5, pady=(0,5), sticky="nsew")
    
    def winSettings(self):
        self.root.title("OShaderIDE")
        self.root.geometry("640x480")
        
        self.root.bind("<Control-s>", self.save)

    def new(self):
        self.current_file = ""
        self.frageditor.delete("1.0", END)
        self.verteditor.delete("1.0", END)
        self.updatePath()
    
    def open(self):
        path = askopenfilename(filetypes=[("Shader", "*.oshader"), ("Any", "*.*")])
        if not path:
            return
        
        self.new()
        
        with open(path, "r") as f:
            data = json.load(f)
            
        self.current_file = path
        
        self.updatePath()
        
        try:    
            frag_bytes = base64.b64decode(data["f"])
            vert_bytes = base64.b64decode(data["v"])
            
            frag_dec = lzma.decompress(frag_bytes).decode("utf-8")
            vert_dec = lzma.decompress(vert_bytes).decode("utf-8")
            
            self.frageditor.insert("1.0", frag_dec)
            self.verteditor.insert("1.0", vert_dec)
        except Exception as ex:
            showerror("Error", f"Error:{ex}")

    def save(self, event=None):
        if self.current_file == "":
            path = asksaveasfilename(defaultextension=".oshader", filetypes=[("Shader", "*.oshader")])
            if not path:
                return
            self.current_file = path
        
        try:
            frag_comp = lzma.compress(self.frageditor.get("1.0", END).encode("utf-8"))
            vert_comp = lzma.compress(self.verteditor.get("1.0", END).encode("utf-8"))
            
            data = {
                "f": base64.b64encode(frag_comp).decode("ascii"),
                "v": base64.b64encode(vert_comp).decode("ascii")
            }
            
            with open(self.current_file, "w") as f:
                json.dump(data, f)
        except Exception as ex:
            showerror("Error", f"Error:{ex}")
    
    def updatePath(self):
        import Utils.manager
        Utils.manager.file_path = self.current_file

def process():
    global app
    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    thread = threading.Thread(target=process)
    thread.start()
    import Utils.shaderviewer