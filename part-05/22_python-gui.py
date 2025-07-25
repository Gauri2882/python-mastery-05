""" Simple Login System """

import tkinter as tk
from tkinter import messagebox

# main window
root = tk.Tk()
root.title("Simple Login System")
root.geometry("300x300")
root.configure(bg = "#f0f4c3")

# predefined credentials
USER_CREDENTIAL = {
    "admin": "admin123", 
    "user": "user123", 
}

# title label
title_label = tk.Label(root, text = "Login System", font = ("Arial", 20), bg = "#f0f4c3")
title_label.pack(pady = 20)

# username input
username_label = tk.Label(root, text = "Username:", font = ("Arial", 12), bg = "#f0f4c3")
username_label.pack()

username_entry = tk.Entry(root, font = ("Arial", 12))
username_entry.pack(pady = 5)

# password entry
password_label = tk.Label(root, text = "Password:", font = ("Arial", 12), bg = "#f0f4c3")
password_label.pack()

password_entry = tk.Entry(root, font = ("Arial", 12), show = "⁘")
password_entry.pack(pady = 5)

# Login function
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username in USER_CREDENTIAL and USER_CREDENTIAL[username] == password:
        messagebox.showinfo("Login Success", f"Welcome, {username}")
    else:
        messagebox.showerror("Login Failed", "Username/Password is incorrect")

# clear function
def clear():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# buttons
login_button = tk.Button(root, text = "Login", command = login, font = ("Arial", 12), bg = "#4caf50", fg = "black")
login_button.pack(pady = 10)

# clear button
clear_button = tk.Button(root, text = "Clear", command = clear, font = ("Arial", 12), bg = "#f44336", fg = "black")
clear_button.pack(pady = 5)

# exit button
exit_button = tk.Button(root, text = "Exit", command = root.destroy, font = ("Arial", 12), bg = "#607d8b", fg = "black")
exit_button.pack(pady = 10)

# run the application
root.mainloop()