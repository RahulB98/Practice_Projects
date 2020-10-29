from tkinter import *
import pyttsx3

root = Tk()
root.title("Text To Speech")
root.iconbitmap('C:/Users/messi/Downloads/favicon.ico')
root.geometry("400x400")

def talk():
    engine = pyttsx3.init()
    engine.setProperty('rate', 100)
    engine.say(my_box.get())
    engine.runAndWait()
    my_box.delete(0,END)

my_box = Entry(root, font=("Helvetica", 18))
my_box.pack(pady=10)

my_button = Button(root, text="Say", command=talk)
my_button.pack()

root.mainloop()
