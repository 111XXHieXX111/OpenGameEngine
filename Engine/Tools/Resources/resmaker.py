from tkinter import *
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import os

class App:
    def __init__(self, master:Tk):
        self.root = master
        
        self.winSettings()

        self.resource_name_frame = Frame(self.root)
        self.resource_name_text = Label(self.resource_name_frame, text="Resource name:")
        self.resource_name_entry = Entry(self.resource_name_frame)

        self.resource_name_frame.pack(side="top", fill="x")
        self.resource_name_text.pack(side="left")
        self.resource_name_entry.pack(side="left", fill="x", expand=True)

        self.select_resource_frame = Frame(self.root)
        self.select_resource_text = Label(self.select_resource_frame, text="Resource:")
        self.select_resource_entry = Entry(self.select_resource_frame)
        self.select_resource_button = Button(self.select_resource_frame, text="...", command=self.selectResource)

        self.select_resource_frame.pack(side="top", fill="x")
        self.select_resource_text.pack(side="left")
        self.select_resource_entry.pack(side="left", fill="x", expand=True)
        self.select_resource_button.pack(side="left")

        self.resource_type_frame = Frame(self.root)
        self.resource_type_text = Label(self.resource_type_frame, text="Resource type:")
        self.resource_type_combobox = Combobox(self.resource_type_frame, state="readonly", values=["Texture", "Sound"])

        self.resource_type_frame.pack(side="top", fill="x")
        self.resource_type_text.pack(side="left")
        self.resource_type_combobox.pack(side="left", fill="x", expand=True)

        self.make_button = Button(self.root, text="Make", command=self.makeResource)
        self.make_button.pack(side="top", fill="x")

    def selectResource(self, event=None):
        filepath = askopenfilename(filetypes=[("Texture", "*.png"), ("Sound", "*.wav"), ("All", "*.*")])
        if not filepath:
            return

        self.select_resource_entry.delete(0, END)
        self.select_resource_entry.insert(0, filepath)

    def makeResource(self, event=None):
        if not self.resource_type_combobox.get():
            showerror("Error", "Select value in combobox")
            return

        respath = self.select_resource_entry.get()
        resname = self.resource_name_entry.get()
        restype = self.resource_type_combobox.get()
        resdata = None

        with open(respath, "rb") as f:
            resdata = f.read()

        if not os.path.exists("Output"):
            os.mkdir("Output")

        with open(f"Output/{resname}.ores", "wb") as f:
            f.write(restype.encode("utf-8"))
            f.write(b"\n")
            f.write(resdata)

    def winSettings(self):
        self.root.title("OResMaker")
        self.root.geometry("320x240")

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
