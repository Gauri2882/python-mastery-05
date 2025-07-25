"""
Handling Mouse Events on Canvas
"""

import tkinter as tk

root = tk.Tk()
root.title("Mouse Drawing")
root.geometry("400x400")

canvas = tk.Canvas(root, width = 400, height = 400, bg = "white")
canvas.pack()

# Draw on mouse drag
def draw(event):
    x, y= event.x, event.y
    canvas.create_oval(x, y, x+2, y+2, fill = "black", outline = "black")

canvas.bind("<B1-Motion>", draw)

root.mainloop()