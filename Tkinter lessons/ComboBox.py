from tkinter import *
from tkinter import ttk

root = Tk()
root.title('ComboBox Keyboard Bind')
root.iconbitmap('C:/Users/messi/Downloads/favicon.ico')

my_label = Label(root)

def myselection(event):
    global my_label
    my_label.destroy()
    if my_CBox.get() == 'Friday':
        my_label = Label(root, text="Yay! It's Friday")
        my_label.grid(row=0, column=1, padx=5)
    else:
        my_label = Label(root, text=my_CBox.get())
        my_label.grid(row=0, column=1, padx=5)
options = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

my_CBox = ttk.Combobox(root, value=options)
my_CBox.current(0)
my_CBox.bind('<<ComboboxSelected>>', myselection)
my_CBox.grid(row=0, column=0, padx=5)

root.mainloop()