""" Different message boxes """

from tkinter import messagebox
import tkinter as tk

root = tk.Tk()
root.withdraw()

# show different message boxes
messagebox.showinfo("Info", "This is an info message")
messagebox.showwarning("Warning", "This is warning message.")
messagebox.showerror("Error", "This is an error message")

response = messagebox.askyesno("Question", "Do you want to continue?")
print("Response:", response)