from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Paned Windows")
root.iconbitmap("C:/Users/messi/Downloads/favicon.ico")
root.geometry("400x400")

def color():
    my_color = colorchooser.askcolor()[1]
    my_color_label = Label(root, text="your colour:" + str(my_color), font=("Helvetica", 30), bg=my_color).pack(pady=5)

my_button = Button(root, text="Choose Color", command=color).pack()


root.mainloop()