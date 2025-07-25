"""
Validating User Input
"""

import tkinter as tk

root = tk.Tk()
root.title("Validating User Input")
root.geometry("300x200")

# Input fields
entry = tk.Entry(root)
entry.pack(pady = 10)

# validate input
def validate_input():
    try:
        value = float(entry.get())
        print(f"Valid Input: {value}")
    except ValueError:
        print("Invalid Input. Please enter a number")

button = tk.Button(root, text = "Validate", command = validate_input)
button.pack(pady = 10)

root.mainloop()