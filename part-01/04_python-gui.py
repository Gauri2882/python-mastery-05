"""
Project: Simple GUI App
"""

import tkinter as tk

root = tk.Tk()
root.title("Simple GUI App")
root.geometry("400x300")
root.configure(bg = "#f0f0f0")

# Title label
title_label = tk.Label(root, text = "Welcome to my GUI App!", font = ("Arial", 18), bg = "#f0f0f0")
title_label.pack(pady = 10)

# Name entry
name_label = tk.Label(root, text = "Enter your name: ", font = ("Arial", 12), bg = "#f0f0f0")
name_label.pack(pady = 10)

name_entry = tk.Entry(root, font = ("Arial", 12), width = 30)
name_entry.pack(pady = 10)

# Greeting function
def greet_user():
    name = name_entry.get()
    if name:
        greeting_label.config(text = f"Hello, {name}!", fg = "green")
    else:
        greeting_label.config(text = "Please enter your name!", fg = "red")

# reset function
def reset():
    name_entry.delete(0, tk.END)
    greeting_label.config(text = "")

# Greet Button
greet_button = tk.Button(root, text = "Greet Me", command = greet_user, font = ("Arial", 12), bg = "#4CAF50", fg = "white")
greet_button.pack(pady = 10)

# Reset Button
reset_button = tk.Button(root, text = "Reset", command = reset, font = ("Arial", 12), bg = "#f44336", fg = "white")
reset_button.pack(pady = 5)

# Greeting label 
greeting_label = tk.Label(root, text = "", font = ("Arial", 14), bg = "#f0f0f0")
greeting_label.pack(pady = 20)

# Run the application
root.mainloop()