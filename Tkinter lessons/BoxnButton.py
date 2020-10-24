from tkinter import *

root = Tk()

e= Entry(root, width= 50)
e.insert(0, "Enter your name: ")
e.pack()

def myclick():
    msg = "Hello " + e.get()
    mylabel= Label(root, text= msg)
    mylabel.pack()

mybutton= Button(root, text= "Submit", command= myclick)
mybutton.pack()

root.mainloop()