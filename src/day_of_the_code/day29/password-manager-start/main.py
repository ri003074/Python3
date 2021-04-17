from tkinter import Tk
from tkinter import Canvas, Label, Entry, Button, W, E, END
from PIL import ImageTk, Image
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    password_list = []

    # for i in range(nr_letters):
    #     password_list.append(random.choice(letters))
    # for i in range(nr_symbols):
    #     password_list.append(random.choice(symbols))
    # for i in range(nr_numbers):
    #     password_list.append(random.choice(numbers))

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    print(password_list)
    random.shuffle(password_list)
    print(password_list)
    password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)

    print(password)

    website_url = website_input.get()
    print(website_url)
    password_result.delete(0, END)
    password_result.insert(END, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():

    if website_input.get() == "" or password_result.get() == "":
        messagebox.showinfo(message="please don't leave blank")
    else:

        is_ok = messagebox.askokcancel(
            title=website_input.get(), message="are you sure to save?"
        )
        if is_ok:
            with open("data.txt", mode="a") as f:
                f.write(
                    f"{website_input.get()} | {password_result.get()} | {email_input.get()}\n"
                )
            password_result.delete(0, END)
            website_input.delete(0, END)


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
website_input.focus()
website_input.grid(row=2, column=1, columnspan=2, sticky=W)

email_label = Label(text="Email/Username: ")
email_label.grid(row=3, column=0)

email_input = Entry(width=35)
email_input.grid(row=3, column=1, columnspan=2, sticky=W)
email_input.insert(END, "kenta@gmail.com")

password_label = Label(text="Password: ")
password_label.grid(row=4, column=0)

password_result = Entry(width=21)
password_result.grid(row=4, column=1, sticky=W)

password_button = Button(text="Generate Paasword", command=generate_password)
password_button.grid(row=4, column=2, sticky=W)

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=5, column=1, columnspan=2, sticky=W + E)


window.mainloop()
