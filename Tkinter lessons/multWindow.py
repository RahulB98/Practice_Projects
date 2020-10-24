from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Multiple Window Program Example")
root.iconbitmap("C:/Users/messi/Downloads/favicon.ico")

def resize(address):
    img = Image.open(address)
    img = img.resize((250, 150))
    return img

def open():
    global img
    top = Toplevel()
    top.title("Window 1")
    top.iconbitmap("C:/Users/messi/Downloads/favicon.ico")

    img = ImageTk.PhotoImage(resize("C:/Users/messi/Pictures/Camera Roll/WIN_20190513_17_11_48_Pro.jpg"))
    Label(top, image=img).pack()
    Button(top, text="close this window", command=top.destroy).pack()

Button(root, text="Open second windo", command=open).pack()



root.mainloop()