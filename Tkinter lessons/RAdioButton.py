from tkinter import *

root = Tk()
root.title("Radio Box Example")
root.iconbitmap("C:/Users/messi/Downloads/favicon.ico")

#r = IntVar()

Toppings = [
    ("Pepperoni","Pepperoni"),
    ("Mushroom","Mushroom"),
    ("Paneer","Paneer"),
    ("Cheese","Cheese"),
    ("Pinapple", "WE DON'T DO IT HERE!")
]

pizza = StringVar()
pizza.set("Pepperoni")

def clicked(value):
    my_label = Label(root, text=value).pack()

for text,topping in Toppings:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

my_button = Button(root, text="Submit", command= lambda : clicked(pizza.get())).pack()

#Radiobutton(root, text="Option 1", variable=r, value=1, command= lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command= lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 3", variable=r, value=3, command= lambda: clicked(r.get())).pack()

#my_label = Label(root, text=pizza.get()).pack()








root.mainloop()
