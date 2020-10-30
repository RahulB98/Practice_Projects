from tkinter import *
from tkinter import ttk
import time

def start():
    for x in range(10):
        my_label.config(text=my_progress['value']+10)
        my_progress['value'] += 10
        root.update_idletasks()
        time.sleep(1)


def stop():
    my_progress.stop()

root = Tk()
root.iconbitmap("C:/Users/messi/Downloads/favicon.ico")
root.title("Progress Bar")
root.geometry("400x400")

my_progress = ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode="determinate")
my_progress.pack(pady=10)

start_button = Button(root, text="Start", command=start)
start_button.pack(pady=5)
stop_button = Button(root, text="Stop", command=stop)
stop_button.pack(pady=5)

my_label = Label(root, text="")
my_label.pack(pady=5)

root.mainloop()