"""
Handling user events
"""

import tkinter as tk

root = tk.Tk()
root.title("Event Handling Example")
root.geometry("300x200")

# Adding widgets
label = tk.Label(root, text = "Enter  your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

def greet():
    name = entry.get()
    label.config(text = f"Hello, {name}!")

button = tk.Button(root, text = "Greet", command = greet)
button.pack()

root.mainloop()