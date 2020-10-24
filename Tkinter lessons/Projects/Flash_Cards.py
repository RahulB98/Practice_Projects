from tkinter import *
from PIL import ImageTk,Image
import random

root = Tk()
root.title('Flash Card')
root.iconbitmap('C:/Users/messi/Downloads/favicon.ico')
root.geometry("600x600")

#image resize
def resize(address):
    img = Image.open(address)
    img = img.resize((300, 250))
    return img

#random state
def random_state():
    #create state list
    global our_states, rando
    our_states = ['arunachalpradesh', 'delhi', 'gujarat', 'himachalpradesh', 'jammuandkashmeer', 'kerala', 'punjab',
                  'rajasthan', 'sikkim', 'tamilnadu', 'uttarpradesh']
    rando = random.randint(0, len(our_states) - 1)

    # show state image
    global state_image
    state_image = ImageTk.PhotoImage(resize('flash_state/' + our_states[rando] + '.png'))
    show_state.config(image=state_image, bg="white")

#create capital answer function
def state_capitals_answer():
    if capital_radio.get() == our_states_capitals[answer]:
        response = "Correct " + our_states_capitals[answer].title() + " is the capital of " + answer.title()
    else:
        response = "Incorrect " + our_states_capitals[answer].title() + " is the capital of " + answer.title()
    capital_answer_label.config(text=response, font=("helvetica", 18))


#create state answer button function
def state_answer():
    answer = answer_input.get()
    answer = answer.replace(" ", "")

    if answer.lower() == our_states[rando]:
        result = "Correct! the answer was " + our_states[rando].title()
    else:
        result = "Incorrect! the answer was " + our_states[rando].title()
    answer_label.config(text=result, font=("Helvetica", 22))
    #reshuffle image
    random_state()
    # delete entry box
    answer_input.delete(0, END)

#create STATE FLASHCARD func
def states():
    #hide previous frame
    hide_all_frames()
    states_frame.pack(fill=BOTH, expand=1)

    '''
    #state list
    global our_states, rando
    our_states = ['arunachalpradesh', 'delhi', 'gujarat', 'himachalpradesh', 'jammuandkashmeer', 'kerala', 'punjab', 'rajasthan', 'sikkim', 'tamilnadu', 'uttarpradesh']
    rando = random.randint(0, len(our_states) - 1)

    #show state image
    global state_image
    state_image = ImageTk.PhotoImage(resize('flash_state/' + our_states[rando] + '.png'))
    '''
    global show_state
    show_state = Label(states_frame)
    show_state.pack(pady=10)
    random_state()

    #create ENTRYBOX to enter answer
    global answer_input
    answer_input = Entry(states_frame, font=("Helvetica", 18), bd=2)
    answer_input.pack(pady=5)

    #create BUTTON to RANDOMIZE state image
    random_state_button = Button(states_frame, text="Pass", command=states)
    random_state_button.pack(pady=5)

    #create BUTTON to recieve answer
    answer_button = Button(states_frame, text="Submit", command=state_answer)
    answer_button.pack(pady=5)

    #create label to tell answer is right or wrong
    global answer_label
    answer_label = Label(states_frame, text="", font=("Helvetica", 18), bg="white")
    answer_label.pack(pady=5)


#create STATE CAPITAL FLASHCARD fun
def state_capitals():
    #hide previous frame
    hide_all_frames()
    state_capitals_frame.pack(fill=BOTH, expand=1)

    global show_state
    show_state = Label(state_capitals_frame)
    show_state.pack(pady=10)

    global our_states, rando
    our_states = ['arunachalpradesh', 'delhi', 'gujarat', 'himachalpradesh', 'jammuandkashmeer', 'kerala', 'punjab',
                  'rajasthan', 'sikkim', 'tamilnadu', 'uttarpradesh']
    global our_states_capitals
    our_states_capitals = {
        'arunachalpradesh': "itanagar",
        'delhi': "delhi",
        'gujarat': "ahemdabad",
        'himachalpradesh': "shimla",
        'jammuandkashmeer': "srinagar",
        'kerala': "thiruvananthapuram",
        'punjab': "chandigarh",
        'rajasthan': "jaipur",
        'sikkim': "gangtok",
        'tamilnadu': "chennai",
        'uttarpradesh': "lucknow"
    }

    #generate three random capitals
    answer_list = []
    for i in range(3):
        rando = random.randint(0, len(our_states) -1)
        if i == 1:
            global answer
            answer = our_states[rando]
            global state_image
            state = 'flash_state/' + our_states[rando] + '.png'
            state_image = ImageTk.PhotoImage(resize(state))
            show_state.config(image=state_image)

        #add to the answerlist
        answer_list.append(our_states_capitals[our_states[rando]])
        #remove state so that it is not repeated
        our_states.remove(our_states[rando])
        #shuffle the state for more randomness
        random.shuffle(our_states)
    random.shuffle(answer_list)

    global capital_radio
    capital_radio = StringVar()
    capital_radio.set(answer_list[0])

    capital_radio_button1 = Radiobutton(state_capitals_frame, text=answer_list[0].title(), variable=capital_radio, value=answer_list[0]).pack()
    capital_radio_button2 = Radiobutton(state_capitals_frame, text=answer_list[1].title(), variable=capital_radio, value=answer_list[1]).pack()
    capital_radio_button3 = Radiobutton(state_capitals_frame, text=answer_list[2].title(), variable=capital_radio, value=answer_list[2]).pack()

    #button to passs
    pass_button = Button(state_capitals_frame, text="Pass", command=state_capitals)
    pass_button.pack(pady=10)
    #button to answer
    capital_answer_button = Button(state_capitals_frame, text="Answer", command=state_capitals_answer)
    capital_answer_button.pack(pady=10)
    #result label
    global capital_answer_label
    capital_answer_label = Label(state_capitals_frame, text="")
    capital_answer_label.pack(pady=10)
#answer of add function
def answer_add():
    answer = num_1 + num_2
    if answer == int(answer_entry.get()):
        response = "Correct " + str(num_1) + " + " + str(num_2) + "  = " + str(answer)
    else:
        response = "Wrong " + str(num_1) + " + " + str(num_2) + " = " + str(answer) + " not " + answer_entry.get()
    add()
    answer_message.config(text=response)

#add function
def add():
    hide_all_frames()
    add_frame.pack(fill=BOTH, expand=1)

    add_label = Label(add_frame, text="Addition Flashcard", font=("helvetica", 18)).pack()
    pic_frame = Frame(add_frame, width=400, height=300)
    pic_frame.pack()

    global num_1, num_2
    num_1 = random.randint(0,10)
    num_2 = random.randint(0,10)
    #content label
    num_1_label = Label(pic_frame)
    math_sign = Label(pic_frame, text=" + ", font=("helvetica", 28))
    num_2_label = Label(pic_frame)

    #gridding content
    num_1_label.grid(row=0, column=0)
    math_sign.grid(row=0, column=1)
    num_2_label.grid(row=0, column=2)

    #image opening
    global image_1, image_2
    image_1 = ImageTk.PhotoImage(Image.open("flash_add/" + str(num_1) + ".png"))
    image_2 = ImageTk.PhotoImage(Image.open("flash_add/" + str(num_2) + ".png"))
    num_1_label.config(image=image_1)
    num_2_label.config(image=image_2)

    #answer entry box and button
    global answer_entry
    answer_entry = Entry(add_frame, font=("helvetica", 18))
    answer_entry.pack(pady=10)
    answer_button = Button(add_frame, text="Answer", command=answer_add)
    answer_button.pack(pady=5)
    global answer_message
    answer_message = Label(add_frame, text="", font=("helvetica", 20))
    answer_message.pack(pady=10)

#HIDE all FRaMES
def hide_all_frames():
    for widget in states_frame.winfo_children():
        widget.destroy()

    for widget in state_capitals_frame.winfo_children():
        widget.destroy()

    for widget in add_frame.winfo_children():
        widget.destroy()

    add_frame.pack_forget()
    states_frame.pack_forget()
    state_capitals_frame.pack_forget()


#create MENU
my_menu = Menu(root)
root.config(menu=my_menu)

#add items to my menu
states_menu = Menu(my_menu)
my_menu.add_cascade(label="Geography", menu=states_menu)
states_menu.add_command(label="States", command=states)
states_menu.add_command(label="State Capital", command=state_capitals)
states_menu.add_separator()
states_menu.add_command(label="Exit", command=root.quit)

#math menu
maths_menu = Menu(my_menu)
my_menu.add_cascade(label="Maths", menu=maths_menu)
maths_menu.add_command(label="Add", command=add)

#create FRAMES
states_frame = Frame(root, width=500, height=500, bg='white')
state_capitals_frame = Frame(root, width=500, height=500)
#addition frame
add_frame = Frame(root, width=500, height=500)

root.mainloop()