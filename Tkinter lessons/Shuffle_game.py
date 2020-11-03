from tkinter import *
import random

root = Tk()
root.title('CRM app')
root.iconbitmap('C:/Users/messi/Downloads/favicon.ico')
root.geometry("800x400")

word_label = Label(root, text="", font=("helvetica", 32))
word_label.pack(pady=20)

def shuffle():
    #clearing box and labels
    my_entry.delete(0,END)
    answer_label.config(text="")

    word_list=["car", "lion", "tiger", "cheetah", "jaguar", "aeroplane", "leopard", "crocodile"]
    global word, jumbled_word
    word = random.choice(word_list)

    jumbled_word = list(word)
    random.shuffle(jumbled_word)
    word_label.config(text="".join(jumbled_word))


def answer():
    if word == my_entry.get():
        answer_label.config(text="Correct answer!")
    else:
        answer_label.config(text="Wronng! The correct answer is " + word)

my_entry = Entry(root, font=("helvetica", 24))
my_entry.pack(pady=10)

button_frame = Frame(root)
button_frame.pack(pady=10)

my_button = Button(button_frame, text="Next Word", command=shuffle)
my_button.grid(row=0, column=0, padx=10)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=1)

answer_label = Label(root, text="", font=("helvetica", 16))
answer_label.pack()

shuffle()

root.mainloop()