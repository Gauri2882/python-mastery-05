""" Using message boxes for validation """

from tkinter import messagebox
import tkinter as tk

root = tk.Tk()
root.title("Validation Example")
root.geometry("300x200")

# label
label = tk.Label(root, text = "Enter your name below", font = ("Arial", 12), fg = "black")
label.pack(pady = 20)

# input field
entry = tk.Entry(root)
entry.pack(pady = 10)

# validate input
def validate_input():
    user_input = entry.get()
    if user_input.strip() == "":
        messagebox.showerror("Error", "तुला तिथे टाक म्हटलं कळत नाही का माकडें")
    else:
        messagebox.showinfo("Success", f"लय शहाणी आहेस!: {user_input}")

# button
button = tk.Button(root, text = "Submit", command = validate_input)
button.pack(pady = 20)

root.mainloop()
