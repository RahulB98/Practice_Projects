from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Notepad And Tabs')
root.iconbitmap('C:/Users/messi/Downloads/favicon.ico')
root.geometry("600x600")

def hide():
    my_notebook.hide(1)

def show():
    my_notebook.add(my_frame2)

def select():
    my_notebook.select(1)

my_notebook = ttk.Notebook(root)
my_notebook.pack()

my_frame1 = Frame(my_notebook, width=500, height=500, bg="blue")
my_frame2 = Frame(my_notebook, width=500, height=500, bg="red")
my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)

my_notebook.add(my_frame1, text="Blue Tab")
my_notebook.add(my_frame2, text="Red Tab")

my_button1 = Button(my_frame1, text="Hide Red Frame", command=hide).pack(pady=5) #to hide tab
my_button2 = Button(my_frame1, text="Show Red Frame", command=show).pack(pady=5) #to show tab
my_button2 = Button(my_frame1, text="Navigate to tab", command=select).pack(pady=5) #to navigate to tab


root.mainloop()