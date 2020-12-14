from tkinter import *
import pygame

root = Tk()
root.title('Souds and Music')
root.iconbitmap('Tkinter lessons/images/favicon.ico')

pygame.mixer.init()

def play():
    pygame.mixer.music.load("Tkinter lessons/music/01. Linkin Park - Numb (Album Version).mp3")
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()

start_button = Button(root, text="Play music", command=play)
start_button.pack(pady=10)

stop_button = Button(root, text="Stop", command=stop)
stop_button.pack(pady=10)
root.mainloop()