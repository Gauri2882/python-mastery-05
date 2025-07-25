"""
Project: BMI Calculator
"""

import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x400")
root.configure(bg = "#f0f4c3")

# title label
title_label = tk.Label(root, text = "BMI Calculator", font = ("Arial", 20), bg = "#f0f4c3")
title_label.pack(pady = 20)

# weight input
weight_label = tk.Label(root, text = "Enter your weight (kg): ", font = ("Arial", 12), bg = "#f0f4c3")
weight_label.pack()

weight_entry = tk.Entry(root, font = ("Arial", 12), width = 15)
weight_entry.pack(pady = 5)

# Height input
height_label = tk.Label(root, text = "Enter you height (m): ", font = ("Arial", 12), bg = "#f0f4c3")
height_label.pack()

height_entry = tk.Entry(root, font = ("Arial", 12), width = 15)
height_entry.pack(pady = 5)

# Result label
result_label = tk.Label(root, text = "", font = ("Arial", 14), bg = "#f0f4c3")
result_label.pack(pady = 20)

# calculate BMI function
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive number")

        bmi = weight / (height ** 2)
        status = ""
        if bmi < 18.5:
            status = "Underweight"
        elif 18.5 <= bmi <= 24.9:
            status = "Normal Weight"
        elif 25 <= bmi <= 29.9:
            status = "Overweight"
        else:
            status = "Obesity"
        
        result_label.config(text = f"BMI: {bmi:.2f}\nStatus: {status}", fg = "green")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and heigh.")

# Buttons
calculate_button = tk.Button(root, text = "Calculate BMI", command = calculate_bmi, font = ("Arial", 12), bg = "#4caf50", fg = "black")
calculate_button.pack(pady = 10)

reset_button = tk.Button(root, text = "Reset", command = lambda: [weight_entry.delete(0, tk.END), height_entry.delete(0, tk.END), result_label.config(text = "")], font = ("Arial", 12), bg = "#f44336", fg = "black")
reset_button.pack()

# run the app
root.mainloop()



