from tkinter import *
from PIL import ImageTk,Image
import random

root = Tk()
root.title('List Box')
root.iconbitmap('C:/Users/messi/Downloads/favicon.ico')
root.geometry("600x600")

def delete():
    for item in reversed(my_listbox.curselection()):
        my_listbox.delete(item)
    show_label.config(text="")

def delete_all():
    my_listbox.delete(0, END)
    show_label.config(text="")

def select():
    t = my_listbox.get(ANCHOR)
    show_label.config(text=t)

def select_all():
    selections = ''
    for item in my_listbox.curselection():
        selections += (str(my_listbox.get(item)) + '\n')
    show_label.config(text=selections)

#frame and scrollbar
my_frame = Frame(root)
my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)
#list box
my_listbox = Listbox(my_frame, width=250, yscrollcommand=my_scrollbar.set, selectmode=MULTIPLE)
my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_frame.pack()

my_listbox.pack(pady=5)


#insert items
items = [int(i) for i in range(0, 20)]

for item in items:
    my_listbox.insert(END, item)

delete_button = Button(root, text="Delete", command=delete)
delete_button.pack(pady=5)

select_button = Button(root, text="Select", command=select)
select_button.pack(pady=5)

delete_all_button = Button(root, text="Delete ALL", command=delete_all)
delete_all_button.pack(pady=5)

select_all_button = Button(root, text="Select ALL", command=select_all)
select_all_button.pack(pady=5)

global show_label
show_label = Label(root, text="")
show_label.pack(pady=5)

root.mainloop()