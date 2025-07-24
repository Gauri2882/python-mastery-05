"""
Binding Events
"""

import tkinter as tk

root = tk.Tk()
root.title("Binding Events")
root.geometry("300x300")

# Event Handlers
def on_enter(event):
    button.config(text = "Cursor is on button")

def on_leave(event):
    button.config(text = "Cursor is not on the button")

# Create Button
button = tk.Button(root, text = "Hover Me")
button.pack(pady = 20)

# Bind Events
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

root.mainloop()