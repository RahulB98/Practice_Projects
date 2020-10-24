from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image move")
root.iconbitmap("C:/Users/messi/Downloads/favicon.ico")
root.geometry("800x600")

def hover(event):
    my_img = PhotoImage(file="images/small.png")
    my_label.config(image=my_img)
    my_label.image = my_img

def hover_back(event):
    my_img = PhotoImage(file="images/very_small.png")
    my_label.config(image=my_img)
    my_label.image = my_img
    
img = PhotoImage(file="images/very_small.png")
my_label = Label(root, image=img)
my_label.pack(pady=20)

my_label.bind("<Enter>", hover)
my_label.bind("<Leave>", hover_back)
root.mainloop()