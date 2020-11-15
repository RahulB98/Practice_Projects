from tkinter import *
from tkcalendar import *

root = Tk()
root.title("Image move")
root.iconbitmap("C:/Users/messi/Downloads/favicon.ico")
root.geometry("800x600")

my_calendar = Calendar(root, selectmode="day", year=2020, month=9, day=28)
my_calendar.pack(pady=10)

def get_date():
    date_label.config(text=my_calendar.get_date())

date_button = Button(root, text="Get Date", command=get_date)
date_button.pack(pady=5)
date_label = Label(root, text="")
date_label.pack(pady=10)

root.mainloop()