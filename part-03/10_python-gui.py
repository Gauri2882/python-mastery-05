"""
Input fields in Tkinter
"""

import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Input Fields Example")
root.geometry("300x200")

# Input fields
entry = tk.Entry(root, width = 25)
entry.pack(pady = 10)

# Button to display input
def display_input():
    user_input = entry.get()
    print("User Input: ", user_input)

button = tk.Button(root, text = "Submit", command = display_input)
button.pack(pady = 10)

# run application
root.mainloop()