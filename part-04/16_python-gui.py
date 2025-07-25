"""
Clearing and Resetting the canvas
"""

import tkinter as tk

root = tk.Tk()
root.title("Clear Canvas")
root.geometry("400x470")

canvas = tk.Canvas(root, width = 400, height = 400, bg = "white")
canvas.pack()

# drawing function
def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x+2, y+2, fill = "black", outline= "black")

# clear function
def clear_canvas():
    canvas.delete("all")

# Bind drawing
canvas.bind("<B1-Motion>", draw)

# clear button
clear_btn = tk.Button(root, text = "Clear", command = clear_canvas)
clear_btn.pack(pady = 10)

root.mainloop()