import tkinter as tk
from tkinter import messagebox

def convert_length():
    try:
        inches = float(entry_inches.get())
        cm = inches * 2.54
        result_var.set(f"{cm:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!.")

root = tk.Tk()
root.title("Length Converter")
root.geometry("450x300")
root.config(bg="#f0f4f7")

title_label = tk.Label(
    root,
    text="Inches to Centimeters Converter",
    font=("Arial", 16, "bold"),
    bg="#f0f4f7",
    fg="#333"
)
title_label.pack(pady=10)

frame = tk.Frame(root, bg="#f0f4f7")
frame.pack(pady=10)

label_inches = tk.Label(
    frame,
    text="Enter length in inches: ",
    font=("Arial", 12),
    bg="#f0f4f7",
)
label_inches.grid(row=0, column=0, padx=5, pady=5)

entry_inches = tk.Entry(
    frame,
    font=("Arial", 12),
    width=15
)
entry_inches.grid(row=0, column=1, padx=10)

convert_btn = tk.Button(
    root,
    text="Convert",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5,
    command=convert_length
)
convert_btn.pack(pady=15)

result_var = tk.StringVar()
result_label = tk.Label(
    root,
    textvariable=result_var,
    font=("Arial", 14, "bold"),
    bg="#f0f4f7",
    fg="#007acc"
)
result_label.pack(pady=10)

root.mainloop()