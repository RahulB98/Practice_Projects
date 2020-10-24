from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title("Image move")
root.iconbitmap("C:/Users/messi/Downloads/favicon.ico")
root.geometry("800x600")

def open_program():
    my_program = filedialog.askopenfilename()
    my_label.config(text=my_program)
    #open the address of program in my_program
    os.system('"%s"' % my_program)

my_button = Button(root, text="Open Promgram", command=open_program)
my_button.pack(pady=10)

my_label = Label(root, text="", font=("Helvetica", 20))
my_label.pack(pady=10)


root.mainloop()