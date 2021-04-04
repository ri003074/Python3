import os
from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter import StringVar
from tkinter import filedialog

BG_COLOR = "#5EAAA8"


class GetPath:
    def __init__(self):
        self.folder_path = os.getcwd()
        self.create_widget()

    def create_widget(self):
        self.window = Tk()
        self.window.title("Get Path GUI")
        self.window.config(padx=50, pady=20)
        self.window.config(bg=BG_COLOR)
        self.folder_path_var = StringVar()
        self.folder_path_var.set(os.getcwd())

        folder_path_label = Label(
            textvariable=self.folder_path_var, bg=BG_COLOR, padx=10, pady=10
        )
        folder_path_label.grid(row=1, column=1)
        select_button = Button(
            self.window,
            text="select dir",
            command=self.browse_button,
            fg=BG_COLOR,
            padx=10,
            pady=10,
        )
        select_button.grid(row=1, column=2)
        exec_button = Button(
            text="exec", command=self.execute, bg=BG_COLOR, padx=10, pady=10
        )
        exec_button.grid(row=1, column=3)

        self.window.mainloop()

    def browse_button(self):
        folder_name = filedialog.askdirectory(initialdir=os.getcwd())
        self.folder_path_var.set(folder_name)
        self.folder_path = folder_name

    def execute(self):
        self.window.destroy()


if __name__ == "__main__":
    get_path = GetPath()
    print(get_path.folder_path)
