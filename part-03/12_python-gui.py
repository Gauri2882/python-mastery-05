"""
Dynamic Results
"""
import tkinter as tk

root = tk.Tk()
root.title("Dynamic Result Display")
root.geometry("300x200")

# input field
entry = tk.Entry(root)
entry.pack(pady = 10)

# result label
result_label = tk.Label(root, text = "Results will be displayed here.")
result_label.pack(pady = 10)

# update label
def update_label():
    text = entry.get()
    result_label.config(text = f"You entered: {text}")

button = tk.Button(root, text = "Update", command = update_label)
button.pack(pady = 10)

root.mainloop()