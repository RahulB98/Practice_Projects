from tkinter import *

root = Tk()
root.title("Image move")
root.iconbitmap("C:/Users/messi/Downloads/favicon.ico")
root.geometry("800x600")

w = 600
h = 400
x = w/2
y = h/2

my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=10)

#Add Image to canvas
img = PhotoImage(file="images/very_small.png", )
my_image = my_canvas.create_image(250, 150, anchor=NW, image=img)

def left(event):
    x = -10
    y = 0
    my_canvas.move(my_image, x, y)

def right(event):
    x = 10
    y = 0
    my_canvas.move(my_image, x, y)

def up(event):
    x = 0
    y = -10
    my_canvas.move(my_image, x, y)

def down(event):
    x = 0
    y = 10
    my_canvas.move(my_image, x, y)

def pressing(event):
    x = 0
    y = 0
    if event.char == "a": x = -10
    if event.char == "d": x = 10
    if event.char == "w": y = -10
    if event.char == "s": y = 10
    my_canvas.move(my_image, x, y)

def move(event):
    my_label.config(text="Position X: " + str(event.x) + " and Y: " + str(event.y))
    global img
    img = PhotoImage(file="images/very_small.png", )
    my_image = my_canvas.create_image(event.x, event.y, image=img)
root.bind("<Key>", pressing)
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)

my_label = Label(root, text="")
my_label.pack(pady=10)

root.bind("<B1-Motion>", move)

root.mainloop()