from tkinter import *
import pygame

root = Tk()
root.title('Souds and Music')
root.iconbitmap('Tkinter lessons/images/favicon.ico')
root.geometry("400x400")

#initializing pygame mixer so that we are able to use it
pygame.mixer.init() 

#create playlist box
song_box = Listbox(root, bg="black", fg="orange", width=60)
song_box.pack(pady=20)

#define player control button
back_button_img = PhotoImage(file="Projects/mp3_player/button_images/backward.png") 
forward_button_img = PhotoImage(file="Projects/mp3_player/button_images/forward.png")
play_button_img = PhotoImage(file="Projects/mp3_player/button_images/play.png")
pause_button_img = PhotoImage(file="Projects/mp3_player/button_images/pause.png")

#create player button frame
button_frame = Frame(root)
button_frame.pack()

#create player control buttons
back_button = Button(button_frame, image=back_button_img , borderwidth=0)
forward_button = Button(button_frame, image=forward_button_img , borderwidth=0)
play_button = Button(button_frame, image=play_button_img , borderwidth=0)
pause_button = Button(button_frame, image=pause_button_img , borderwidth=0)

back_button.grid(row=0, column=0)
forward_button.grid(row=0, column=1)
play_button.grid(row=0, column=2)
pause_button.grid(row=0, column=3)


root.mainloop()