import tkinter as tk
from tkinter import messagebox

def calculate_cube():
    try:
        num = float(entry1.get())
        Cube = num * num * num
        result_label.config(text=f"Cube: {Cube}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

root = tk.Tk()
root.title("Cube Calculator")
root.geometry("300x200")

label1 = tk.Label(root, text="Enter a number: ")
label1.pack(pady=5)

entry1 = tk.Entry(root)
entry1.pack(pady=5)

calc_button = tk.Button(root, text="Calculate Cube", command=calculate_cube)
calc_button.pack(pady=10)

result_label = tk.Label(root, text="Cube: ")
result_label.pack(pady=5)

root.mainloop()