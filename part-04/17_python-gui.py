"""
Project: Drawing Pad App
"""

import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title("Drawing Pad App")
root.geometry("600x600")
root.configure(bg = "#f0f0f0")

# Global Variables
current_color = "black"
current_thickness = 2

# Create canvas
canvas = tk.Canvas(root, width = 500, height = 400, bg = "white", relief = "ridge", bd = 2)
canvas.pack(pady = 20)

# drawing function
def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(
        x - current_thickness, y - current_thickness,
        x + current_thickness, y + current_thickness, 
        fill = current_color, outline = current_color
    )

# clear canvas
def clear_canvas():
    canvas.delete("all")

# change color
def change_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color

# change thickness
def change_thickness(value):
    global current_thickness
    current_thickness = int(value)

# bind drawing
canvas.bind("<B1-Motion>", draw)

# control panel
control_frame = tk.Frame(root, bg = "#f0f0f0")
control_frame.pack(pady = 10)

# color button
color_btn = tk.Button(control_frame, text = "Choose color", command = change_color, bg = "#4caf50", fg = "black", font = ("Arial", 10))
color_btn.grid(row = 0, column = 0, padx = 10)

# clear button
clear_btn = tk.Button(control_frame, text = "Clear canvas", command = clear_canvas, bg = "#f44336", fg = "black", font = ("Arial", 10))
clear_btn.grid(row = 0, column = 1, padx = 10)

# thickness control
thickness_label = tk.Label(control_frame, text = "Thickness", bg = "#f0f0f0", font = ("Arial", 10))
thickness_label.grid(row = 0, column = 2, padx = 10)

thickness_slider = tk.Scale(control_frame, from_ = 1, to = 10, orient = "horizontal", command = change_thickness, bg = "#f0f0f0")
thickness_slider.set(2)
thickness_slider.grid(row = 0, column = 3, padx = 10)

# run the app
root.mainloop()