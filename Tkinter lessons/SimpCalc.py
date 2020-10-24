from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(column=0, row=0, columnspan=4, padx= 10, pady=10)

def button_click(number):
    e.insert(END, number)
    return

def button_clear():
    e.delete(0, END)

def button_symbol(symbol):
    first_number = int(e.get())
    e.delete(0, END)
    global f_num , sym
    f_num = first_number
    sym = str(symbol)

def button_equal():
    second_number = int(e.get())
    e.delete(0,END)
    if sym == "+":
        e.insert(0, f_num + second_number)
    elif sym == "*":
        e.insert(0, float(f_num * second_number))
    elif sym == "-":
        e.insert(0, f_num - second_number)
    elif sym == "/":
        e.insert(0, float(f_num / second_number))

#Defining buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

add_button = Button(root, text="+", padx=40, pady=20, command=lambda: button_symbol("+"))
sub_button = Button(root, text="-", padx=40, pady=20, command=lambda: button_symbol("-"))
mul_button = Button(root, text="*", padx=40, pady=20, command=lambda: button_symbol("*"))
div_button = Button(root, text="/", padx=40, pady=20, command=lambda: button_symbol("/"))

equal_button = Button(root, text="=", padx=100, pady=20, command=lambda: button_equal())
clear_button = Button(root, text="Clear", padx=80, pady=20, command=lambda: button_clear())


#put buttons on to the screen
button_1.grid(column=0, row=1)
button_2.grid(column=1, row=1)
button_3.grid(column=2, row=1)
add_button.grid(row=1, column=3)

button_4.grid(column=0, row=2)
button_5.grid(column=1, row=2)
button_6.grid(column=2, row=2)
sub_button.grid(row=2, column=3)

button_7.grid(column=0, row=3)
button_8.grid(column=1, row=3)
button_9.grid(column=2, row=3)
mul_button.grid(row=3, column=3)

button_0.grid(column=0, row=4)
div_button.grid(row=4, column=1)
clear_button.grid(row=4, column=2, columnspan=2)

equal_button.grid(row=6, column=0, columnspan=4)

root.mainloop()



