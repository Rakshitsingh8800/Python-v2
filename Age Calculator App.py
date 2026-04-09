from tkinter import *

root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")

frame = Frame(master=root, height=200, width=360, bg="lightblue")

lbl1 = Label(frame, text="Enter Your Birth Year", bg="lightblue", fg="white", width=20)
lbl2 = Label(frame, text="Enter Current Year", bg="lightblue", fg="white", width=20)
lbl3 = Label(frame, text="Your Age is", bg="lightblue", fg="white", width=20)

def calculate_age():
    birth_year = int(birth_year_entry.get())
    current_year = int(current_year_entry.get())
    age = current_year - birth_year
    age_entry.delete(0, END)
    age_entry.insert(0, str(age))
birth_year_entry = Entry(frame)
current_year_entry = Entry(frame)
age_entry = Entry(frame)

btn = Button(text = "Calculate Age", command=calculate_age, bg="red")


frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
birth_year_entry.place(x=200, y=20)
lbl2.place(x=20, y=80)
current_year_entry.place(x=200, y=80)
lbl3.place(x=20, y=140)
age_entry.place(x=200, y=140)
btn.place(x=130, y=210)

root.mainloop()

