from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Message Box Example")
root.iconbitmap("C:/Users/messi/Downloads/favicon.ico")

def popup():
    response = messagebox.askyesno("Title", "Hey There!")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked Yes").pack()
    else:
        Label(root, text="You clicked NO").pack()

Button(root, text="Pop UP", command= lambda :popup()).pack()







root.mainloop()