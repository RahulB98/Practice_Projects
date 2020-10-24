from tkinter import *

root = Tk()
root.title("Weather App")
root.iconbitmap("C:/Users/messi/Downloads/favicon.ico")
root.geometry("400x100")

def clicked(event):
    mylabel = Label(root, text="Button clicked: " + str(event.keysym))
    mylabel.pack()

mybutton = Button(root, text="Bind")
mybutton.bind("<Key>", clicked)
mybutton.pack()

root.mainloop()