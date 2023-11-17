from tkinter import *

def mile_to_km():
    mile = int(mile_input.get())
    km = round(mile * 1.609)
    result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to kilometer converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


mile_input = Entry(window, width=10)
mile_input.grid(column=1, row=0)

Mile_label = Label(window, text="Miles")
Mile_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to ")
is_equal_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

kilometer_label = Label(text="KM")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="calculate", command=mile_to_km)
calculate_button.grid(column=1, row=2)


mainloop()