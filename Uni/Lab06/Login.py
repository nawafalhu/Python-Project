import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as fd

def check_phone_number():
    phone_number = phone_number_entry.get()

    if len(phone_number) != 10 and phone_number[0] != 0 and phone_number[1] != 5:
        tk.Messagebox.showerror(title="Error", message="Invalide Phone Number")

def upload_photo(): 
    filepath = fd.askopenfilename(title="Select a photo", filetypes=[("Image files", "*.jpg *.png *.gif")])

def select_file():
    filepath = fd.askopenfilename(title="Select a file")

def check_input():
    user_input = full_name_entry.get()

    if type(user_input) != str:
        tk.Messagebox.showerror(title="Error", message="Invalide Name")

def clear_window():
    full_name_entry.delete(0, 'end')
    id_entry.delete(0, 'end')
    phone_number_entry.delete(0, 'end')
    salary_entry.delete(0, 'end')
    file_entry.delete(0, "end")

def store_information():
    check_input()
    full_name = full_name_entry.get()
    id = id_entry.get()
    phone_number = phone_number_entry.get()
    salary = salary_entry.get()
    file_path = file_entry.get()

    with open(file_path, "a") as f:
        f.write(f"{full_name},{id},{phone_number},{salary}\n")
    clear_window()



root = tk.Tk()
root.title("Employment Form")
# change the back ground color

form_frame = ttk.Frame(root)
form_frame.pack()

image = tk.PhotoImage(file=r"D:\Python-Project\Uni\Lab06\images.png")
label = tk.Label(form_frame, image=image)
label.grid(row=0, column=0)

upload_image_button = ttk.Button(form_frame, text="Upload Image", command=upload_photo)
upload_image_button.grid(row=0, column=3)

full_name_label = tk.Label(form_frame, text="Full Name:")
full_name_label.grid(row=2, column=0)
#
full_name_entry = ttk.Entry(form_frame)
full_name_entry.grid(row=2, column=3)

id_label = tk.Label(form_frame, text="ID:")
id_label.grid(row=4, column=0)
#
id_entry = ttk.Entry(form_frame)
id_entry.grid(row=4, column=3)

phone_number_label = tk.Label(form_frame, text="Phone Number:")
phone_number_label.grid(row=6, column=0)
#
phone_number_entry = ttk.Entry(form_frame)
phone_number_entry.grid(row=6, column=3)

salary_label = tk.Label(form_frame, text="Salary:")
salary_label.grid(row=8, column=0)
#
salary_entry = ttk.Entry(form_frame)
salary_entry.grid(row=8, column=3)

team_label = tk.Label(form_frame, text="Team:")
team_label.grid(row=10, column=0)
#
team_radio_buttons = ttk.Radiobutton(form_frame, text="Engineering", value="engineering")
team_radio_buttons.grid(row=10, column=3)

team_radio_buttons = ttk.Radiobutton(form_frame, text="Sales", value="sales")
team_radio_buttons.grid(row=10, column=4)

team_radio_buttons = ttk.Radiobutton(form_frame, text="Marketing", value="marketing")
team_radio_buttons.grid(row=10, column=5)

file_label = tk.Label(form_frame, text="File to save:")
file_label.grid(row=12, column=0)
#
file_entry = ttk.Entry(form_frame)
file_entry.grid(row=12, column=3)

file_button = ttk.Button(form_frame, text="Open",command=select_file)
file_button.grid(row=12, column=4)

submit_button = ttk.Button(form_frame, text="Submit", command=store_information)
submit_button.grid(row=15, column=1)
root.mainloop()