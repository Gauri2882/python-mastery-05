"""
Canvas Widgets
"""

import tkinter as tk

# main window
root = tk.Tk()
root.title("Canvas Example")
root.geometry("400x400")

# create canvas
canvas = tk.Canvas(root, width = 400, height = 300, bg = "white")
canvas.pack()

# Draw shapes
canvas.create_line(10, 10, 200, 200, fill = "blue", width = 3)
canvas.create_rectangle(50, 50, 150, 150, outline = "red", width = 2)
canvas.create_oval(200, 50, 350, 200, outline = "green", width = 2)

root.mainloop()