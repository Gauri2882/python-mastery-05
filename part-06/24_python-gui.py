""" Scorllbar Integration """

import tkinter as tk

root = tk.Tk()
root.title("List with scrollbar")
root.geometry("300x300")

# frame for listbox and scrollbar
frame = tk.Frame(root)
frame.pack(pady = 10)

# scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

# listbox
listbox = tk.Listbox(frame, yscrollcommand = scrollbar.set, height = 10)
listbox.pack()

# configure scrollbar
scrollbar.config(command = listbox.yview)

# add items
for i in range(1, 21):
    listbox.insert(tk.END, f"Item {i}")

root.mainloop()
