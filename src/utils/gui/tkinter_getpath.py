import os
from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter import StringVar
from tkinter import filedialog


class GetPath:
    def __init__(self):
        self.folder_path = os.getcwd()
        self.create_widget()

    def create_widget(self):
        self.window = Tk()
        self.window.title("Get Path GUI")
        self.window.config(padx=50, pady=20)
        self.folder_path_var = StringVar()
        self.folder_path_var.set(os.getcwd())

        folder_path_label = Label(textvariable=self.folder_path_var)
        folder_path_label.grid(row=1, column=1)
        select_button = Button(text="select dir", command=self.browse_button)
        select_button.grid(row=1, column=2)
        exec_button = Button(text="exec", command=self.execute)
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
