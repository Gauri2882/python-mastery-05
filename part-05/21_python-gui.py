""" Handling User authentication """

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Simple Login")
root.geometry("300x200")

# user credentials
USERNAME = "admin"
PASSWORD = "password9520"

# Labels and entry fields
tk.Label(root, text = "Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text = "Password:").pack()
password_entry = tk.Entry(root, show = "♪")
password_entry.pack()

# authentication functions
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == USERNAME and password == PASSWORD:
        messagebox.showinfo("Login Success", "जास्त धडे नको शिकवू!")
    else:
        messagebox.showerror("Login Failed", "सांगितलेलं लक्षात नाही राहत का?")

# login button
login_btn = tk.Button(root, text = "Login", command = login)
login_btn.pack(pady = 10)

# run app
root.mainloop()
