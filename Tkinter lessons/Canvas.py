from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Canvas')
root.iconbitmap('C:/Users/messi/Downloads/favicon.ico')
root.geometry("600x600")
#create canvas
my_canvas = Canvas(root, width=500, height=500, bg="white")
my_canvas.pack(pady=5)

#draw on canvas
#create rectangle
#my_canvas.create_rectangle(x1, y1, x2, y2, fill="red")
#x1,y1 : top left, x2,y2 : bottom right
my_canvas.create_rectangle(50, 450, 450, 50, fill="pink")

#create oval
my_canvas.create_oval(50, 450, 450, 50, fill="cyan")

#create line
#my_canvas.create_line(x1, y1, x2, y2, fill="red")
#x1,y1 : start point , x2,y2 : end point
my_canvas.create_line(0, 250, 500, 250, fill="red")
my_canvas.create_line(250, 0, 250, 500, fill="red")

root.mainloop()