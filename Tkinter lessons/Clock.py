from tkinter import *
import time

root = Tk()
root.title('CRM app')
root.iconbitmap('C:/Users/messi/Downloads/favicon.ico')
root.geometry("400x400")

def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    am_pm = time.strftime("%p")
    day = time.strftime("%A")
    time_zone = time.strftime("%Z")

    time_label.config(text=hour + ":" + minute + ":" + second + am_pm)
    time_label.after(1000, clock)

    day_label.config(text=time_zone + ", " +day)

time_label = Label(root, text="", font=("helvetica", 48), fg="green", bg="black")
time_label.pack(pady=10)
day_label = Label(root, text="")
day_label.pack(pady=5)

clock()

root.mainloop()