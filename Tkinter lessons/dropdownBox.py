from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("CheckBox")
root.iconbitmap("C:/Users/messi/Downloads/favicon.ico")
root.geometry("400x400")

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]
choose = StringVar()
choose.set(options[0])

drop = OptionMenu(root, choose, *options).pack()

def btn():
    Label(root, text=choose.get()).pack()

Button(root, text="Show Selection", command=btn).pack()

root.mainloop()