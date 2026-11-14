from tkinter import *
import calendar
from tkinter import messagebox
screen=Tk()
screen.title("calendar")
screen.geometry("650x600")
cal=calendar.TextCalendar(firstweekday=0)
#month_cal_str=cal.formatmonth(year, month)

def showcalander():
    y=Year.get()
    m=Month.get()
    if not y.isdigit() or not m.isdigit():
        messagebox.showerror("ERROR", "Please enter the valid details.")
    y=int(y)
    m=int(m)
    if y<1 or y>9999 or m<1 or m>12:
        messagebox.showerror("ERROR", "Please enter a valid number.")
    c=calendar.calendar(y)
    #cal=calander.calendar(f, year=y, month=m, selectmode="day")
    #cal.pack()
    print(calendar.month(y, m))
    print(calendar.isleap(y))
    print(calendar.weekday(y, m, 14))
    print(calendar.monthrange(y, m))
    month=(calendar.month(y, m))
    text.delete("1.0", END)
    text.insert(END, month)

Label(screen, text="Welcome to Calendar").pack(pady=20)
Label(screen, text="Enter the Year").pack(pady=20)
Year=Entry(screen)
Year.pack(pady=20)
Month=Entry(screen)
Month.pack(pady=20)
Button(screen, text="Click Here", command=showcalander).pack(pady=20)
f=Frame(screen)
f.pack(padx=20, pady=20, fill=BOTH, expand=True)
text=Text(f)
text.pack(pady=10, fill=BOTH, expand=True)
screen.mainloop()