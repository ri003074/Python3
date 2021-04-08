from tkinter import Tk
from tkinter import Canvas, Label, Entry, Button, W, E
from PIL import ImageTk, Image

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Pass Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
# mypass_img = ImageTk.PhotoImage(file="logo.png")
mypass_img = ImageTk.PhotoImage(Image.open("logo.png").convert("RGB"))

canvas.create_image(100, 100, image=mypass_img)
canvas.grid(row=1, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=2, column=0)

website_input = Entry(width=35)
website_input.grid(row=2, column=1, columnspan=2, sticky=W)

email_label = Label(text="Email/Username: ")
email_label.grid(row=3, column=0)

email_input = Entry(width=35)
email_input.grid(row=3, column=1, columnspan=2, sticky=W)

password_label = Label(text="Password: ")
password_label.grid(row=4, column=0)

password_input = Entry(width=21)
password_input.grid(row=4, column=1, sticky=W)

password_button = Button(text="Generate Paasword")
password_button.grid(row=4, column=2, sticky=W)

add_button = Button(text="Add", width=36)
add_button.grid(row=5, column=1, columnspan=2, sticky=W + E)

window.mainloop()
