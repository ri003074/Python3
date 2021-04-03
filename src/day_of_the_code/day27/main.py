from tkinter import Tk, Button, Label, Entry

windown = Tk()
windown.title("My First GUI Program")
windown.minsize(width=500, height=300)

my_label = Label(text="I am Label", font=("Arial", 24, "bold"))
my_label.pack(side="top")


def button_clicked():
    my_label["text"] = input.get()


input = Entry(width=10)
input.pack()

button = Button(text="Click Me", command=button_clicked)
button.pack()

windown.mainloop()
