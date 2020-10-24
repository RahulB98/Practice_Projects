from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image Viewer")
root.iconbitmap('C:/Users/messi/Downloads/favicon.ico')
root.geometry("400x400")

def slide():
    Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

Button(root, text="get horizontal position", command=slide).pack()


root.mainloop()