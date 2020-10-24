from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title("Image Viewer")
root.iconbitmap('C:/Users/messi/Downloads/favicon.ico')

def resize(address):
    img = Image.open(address)
    img = img.resize((250, 150))
    return img

def open():
    global img
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/messi/Pictures/Camera Roll", title="Select A File",
                                               filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    print("filwname= " + str(root.filename))
    my_label = Label(root, text=root.filename).pack()
    img = ImageTk.PhotoImage(resize(root.filename))
    my_image = Label(image=img).pack()

Button(root, text="Open File", command=open).pack()
root.mainloop()