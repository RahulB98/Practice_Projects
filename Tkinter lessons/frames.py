from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("frames")
root.iconbitmap("C:/Users/messi/Downloads/favicon.ico")

frame = LabelFrame(root, padx=10, pady=10)
frame.pack(padx=50, pady=50)

b1 = Button(frame, text="Do Not Click")
b2 = Button(frame, text="....or here")
b1.grid(row=0, column=0)
b2.grid(row=1, column=2)
root.mainloop()
