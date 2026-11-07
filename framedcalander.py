from tkinter import *
import calendar
from tkinter import messagebox
screen=Tk()
screen.title("calander")
screen.geometry("650x600")

def showcalander():
    y=Year.get()
    if not y.isdigit():
        messagebox.showerror("ERROR", "Please enter a valid year.")
    y=int(y)
    if y<1 or y>9999:
        messagebox.showerror("ERROR", "Please enter a number from 1-9999.")
    c=calendar.calendar(y)
    print(c)
    text.delete("1.0", END)
    text.insert(END, c)
Label(screen, text="Welcome to Calander").pack(pady=20)
Label(screen, text="Enter the Year").pack(pady=20)
Year=Entry(screen)
Year.pack(pady=20)
Button(screen, text="Click Here", command=showcalander).pack(pady=20)
f=Frame(screen)
f.pack(padx=20, pady=20, fill=BOTH, expand=True)
text=Text(f)
text.pack(pady=10, fill=BOTH, expand=True)
screen.mainloop()