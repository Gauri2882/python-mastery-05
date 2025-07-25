""" 
Adding widgets (labels, entry fields, button)
"""

import tkinter as tk

# Main window
root = tk.Tk()
root.title("Simple GUI Example")
root.geometry("300x200")

# Add label
label = tk.Label(root, text = "Hello, Tkinter!", font = ("Arial", 14))
label.pack(pady = 10)

# Add entry
entry = tk.Entry(root, width = 20)
entry.pack(pady = 10)

# Add button
def on_click():
    text = entry.get()
    label.config(text = f"Hello, {text}!")

button = tk.Button(root, text = "Click Me", command = on_click)
button.pack(pady = 12)

# Run the application
root.mainloop()

