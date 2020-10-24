import random
choice_array = []

def sortString(str):
    return ''.join(sorted(str))


def listToString(s):
    # initialize an empty string
    str1 = ""

    # return string
    return (str1.join(s))

print("Welcome to the word guessing game")
p_name = input("Please enter your name: ")
print("Hello " + str(p_name) + "! It's time to play the Word Guess game!!")
w_file = open("words.txt")
for line in w_file:
    w_data = line.split(',')
word = random.choice(w_data)
word = word.lower()
attempts = 10
print("The word has "+ str(len(word)) + " letters")
while attempts != 0:
    print("Attempts left: ", attempts, " choices made: ", choice_array.sort())
    choice = input("Enter you guess letter: ")
    if choice in word:
        print(str(choice)+" is in the word")
        choice_array.append(choice)
        #print(sortString(word))
        print(listToString(choice_array))
        if sortString(listToString(choice_array)) == sortString(word):
            print("Great work! You have guessed all the letters in the word")

            word_attempt = 3
            while word_attempt != 0:
                print("Attempts left to guess the word: ", word_attempt)
                choice_word = input("Now enter the word: ")
                if choice_word == word:
                    print("Congratulations You have guessed the word correctly")
                    attempts = 0
                    break
                else:
                    word_attempt -= 1
                    print("sorry wrong word!")
    else:
        print(str(choice)+" is NOT the word")
        attempts -= 1



    if attempts == 0:
        break