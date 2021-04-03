from tkinter import Tk, Button, Label, Entry

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

my_label = Label(text="I am Label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)


def button_clicked():
    my_label["text"] = input.get()


input = Entry(width=10)
input.grid(row=4, column=4)

button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)
new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(row=3, column=1)

window.mainloop()
