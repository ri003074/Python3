from tkinter import Tk, Button, Label, Entry

window = Tk()
window.title("Mile to Km  Converter")
window.config(padx=10, pady=20)


def miles_to_km():
    mile = float(input.get())
    km = mile * 1.609
    km_result.config(text=f"{km}")


input = Entry(width=10)
input.grid(row=1, column=2)

miles = Label(text="Miles", font=("Arial", 12, "bold"))
miles.grid(row=1, column=3)

is_equal = Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal.grid(row=2, column=1)

km_result = Label(text="0", font=("Arial", 12, "bold"))
km_result.grid(row=2, column=2)

km = Label(text="Km", font=("Arial", 12, "bold"))
km.grid(row=2, column=3)


button = Button(text="calc", command=miles_to_km)
button.grid(row=3, column=2)

window.mainloop()
