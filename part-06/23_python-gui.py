""" Advanced Tkinter Widgets"""

import tkinter as tk

root = tk.Tk()
root.title("Listbox example")
root.geometry("300x300")

# Listbox widget
listbox = tk.Listbox(root)
listbox.pack()

# add items to listbox
listbox.insert(tk.END, "Task 1")
listbox.insert(tk.END, "Task 2")

# get selected item
def get_selected():
    selected = listbox.get(tk.ACTIVE)
    print("Selected:", selected)

button = tk.Button(root, text = "Select", command = get_selected)
button.pack(pady = 10)

root.mainloop()