from tkinter import *
import random

root = Tk()
root.title("Random Winner Genertaor")
root.iconbitmap("C:/Users/messi/Downloads/favicon.ico")
root.geometry("400x400")

entries = ['Balbir', 'Sunita', 'Rahul', 'Riya']
def pick(entries):
    entries = set(entries)
    entries = list(entries)
    winner = random.choice(entries)

    winner_label = Label(root, text=winner, font=("Helvetica", 20)).pack()


top_label = Label(root, text="Who's the WINNER!!!!!", font=("Helvetica", 26)).pack(pady=20)

Click = Button(root, text="Show the Winner", font=("Helvetica", 20), command=lambda: pick(entries))
Click.pack(pady=10)

root.mainloop()