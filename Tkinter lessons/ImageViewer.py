from tkinter import *
from PIL import Image, ImageTk

def resize(address):
    img = Image.open(address)
    img = img.resize((250, 150))
    return img


root = Tk()
root.title("Image Viewer")
root.iconbitmap('C:/Users/messi/Downloads/favicon.ico')

my_image1 = ImageTk.PhotoImage(resize("C:/Users/messi/Pictures/Camera Roll/WIN_20190513_17_11_48_Pro.jpg"))
my_image2 = ImageTk.PhotoImage(resize("C:/Users/messi/Pictures/Camera Roll/WIN_20190728_14_29_48_Pro.jpg"))
my_image3 = ImageTk.PhotoImage(resize("C:/Users/messi/Pictures/Camera Roll/WIN_20190728_14_30_08_Pro.jpg"))
my_image4 = ImageTk.PhotoImage(resize("C:/Users/messi/Pictures/Camera Roll/WIN_20190728_14_29_36_Pro.jpg"))
my_image5 = ImageTk.PhotoImage(resize("C:/Users/messi/Pictures/Camera Roll/WIN_20190818_16_51_49_Pro.jpg"))

image_list = [my_image1, my_image2, my_image3, my_image4, my_image5]

my_label = Label(image=my_image1)
my_label.grid(row=0, column=0, columnspan=3)

status = Label(root, text="Images 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor= E)

def forward(image_number): #forward button
    global my_label
    global button_forward
    global button_back

    #defining changes to window
    my_label.grid_forget()
    my_label = Label(root, image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == len(image_list): #check to dosable the forward button after reaching the last image
        button_forward = Button(root, text=">>", state=DISABLED)


    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    #status bar update
    status = Label(root, text="Images" + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

def back(image_number): #back button function
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(root, image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    #updating status bar
    status = Label(root, text="Images" + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

#button creation and showing on screen
button_back = Button(root, text="<<", command=lambda: back(), state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()