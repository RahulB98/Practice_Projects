from tkinter import *

root = Tk()
root.title('ComboBox Keyboard Bind')
root.iconbitmap('C:/Users/messi/Downloads/favicon.ico')
root.geometry("400x400")
def new_file():
    my_label = Label(root, text="HEY!!!!!!!!!!!!")
    my_label.pack()
    return

#Hide all frames
def hide_all_frames():
    for widget in file_new_frame.winfo_children():
        widget.destroy()

    for widget in edit_cut_frame.winfo_children():
        widget.destroy()

    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()

def file_new():
    hide_all_frames()
    file_new_frame.pack(fill="both", expand=1)
    my_label = Label(file_new_frame, text="HEY!!!!!!!!!!!!")
    my_label.pack()

def edit_cut():
    hide_all_frames()
    edit_cut_frame.pack(fill="both", expand=1)
    my_label = Label(edit_cut_frame, text="HEY!!!!!!!!!!!!")
    my_label.pack()

my_menu = Menu(root)
root.config(menu=my_menu)

#Create new menu item as a submenu
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)

file_menu.add_cascade(label="New", command=file_new)
file_menu.add_separator()
file_menu.add_cascade(label="Exit", command=root.quit)

#create Edit menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_cascade(label="Cut", command=edit_cut)
edit_menu.add_separator()
edit_menu.add_cascade(label="Copy", command=new_file)

#create Option menu
option_menu = Menu(my_menu)
my_menu.add_cascade(label="Option", menu=option_menu)

option_menu.add_cascade(label="Find", command=new_file)
option_menu.add_separator()
option_menu.add_cascade(label="Replace", command=new_file)

#Creating FRAMES for menu items
file_new_frame = Frame(root, width=400, height=400, bg="red")
edit_cut_frame = Frame(root, width=400, height=400, bg="blue")

root.mainloop()