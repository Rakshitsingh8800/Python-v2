import tkinter as tk
from datetime import datetime

def calculate_age():
    try:
        dob = datetime.strptime(e.get(), "%d/%m/%Y")
        t = datetime.today()
        age = t.year - dob.year - ((t.month, t.day) < (dob.month, dob.day))
        l.config(text=f"Age: {age} years")
    except:
        l.config(text="Enter in DD/MM/YYYY")

r = tk.Tk()
r.title("Age Calculator")
r.geometry("400x400")

tk.Label(r, text="DOB (DD/MM/YYYY)").pack()
e = tk.Entry(r)
e.pack()

tk.Button(r, text="Calculate", command=calculate_age).pack(pady=5)
l = tk.Label(r)
l.pack()

r.mainloop()
