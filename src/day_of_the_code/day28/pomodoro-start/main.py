from tkinter import Tk
from tkinter import Label
from tkinter import Canvas
from tkinter import Button
from PIL import ImageTk


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 48, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=1, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = ImageTk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="green", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

start_button = Button(text="Start", bg=YELLOW)
start_button.grid(row=3, column=1)
stop_button = Button(text="Stop", bg=YELLOW)
stop_button.grid(row=3, column=3)


check_label = Label(text="✓", font=(FONT_NAME, 48, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(row=4, column=2)

window.mainloop()
