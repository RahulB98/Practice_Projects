from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("CheckBox")
root.iconbitmap("C:/Users/messi/Downloads/favicon.ico")
root.geometry("400x400")

var = StringVar()
c = Checkbutton(root, text="Check if you dare", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()
def show_check():
    check_label = Label(root, text=var.get()).pack()

check_button = Button(root, text="Check Result", command=show_check).pack()

root.mainloop()