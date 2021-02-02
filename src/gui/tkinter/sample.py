from tkinter import StringVar
from tkinter import Tk
from tkinter import filedialog
from tkinter import ttk


class MainFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(padding=(6, 4))
        self.pack(expand=1, fill="x", anchor="n")
        self.make_style()
        self.create_widgets()

    def make_style(self):
        pass

    def create_widgets(self):
        self.label1 = ttk.Label(self, text="File:")
        self.label1.pack(side="left", padx=(0, 2))

        self.entry1_var = StringVar()
        self.entry1 = ttk.Entry(self, textvariable=self.entry1_var, width=32)
        self.entry1.state(["readonly"])
        self.entry1.pack(side="left", expand=1, fill="x", padx=(0, 6))

        self.button1 = ttk.Button(self, text="SAVE", command=self.show_save_dialog)
        self.button1.pack(side="left")

    def show_save_dialog(self):
        ftypes = [
            ("PNG Image Files", ".png"),
            ("SVG Image Files", ".svg .xml"),
            ("All Files", ".*"),
        ]
        ini_fname = "example"
        fname = filedialog.asksaveasfilename(filetypes=ftypes, initialfile=ini_fname)
        if fname:
            self.entry1_var.set(fname)
        else:
            print("Cancel or X button was clicked.")


root = Tk()
root.title("Tkinter win")
frame = MainFrame(root)
frame.mainloop()
