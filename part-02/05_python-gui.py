"""
Button Working
"""

import tkinter as tk

root = tk.Tk()
root.title("Basic Button Example")
root.geometry("300x300")

# Button Click Handler
def on_click():
    print("Button Clicked")

# create button
button = tk.Button(root, text = "Click Me", command = on_click)
button.pack(pady = 20)

# run the application
root.mainloop()