'''
In this project which is a game you should guess the letters untill you find the right letter and become close to win when you find the word befor your tries end.

'''

import random 
from words import word_list 

def get_word () :
    word = random.choice(word_list).upper()
    return word.upper() 

def play (word) :
    guessed_words = []
    guessed_letters = []
    word_code = "_" * len(word) 
    guessed = False 
    tries = 6
    while not guessed and tries >0 :
        x=0
        print( word_code)
        guess = input("put a char or a word : ").upper() 

        if len(guess) == 1 and guess.isalpha(): 
            for char in word :
                if char == guess :
                    x=1
                    print( f"you're right {char} is right letter")
                    guessed_letters.append(char) 
                    incidice = [index for index , letter in enumerate(word)  if letter ==char]
                    word_code_inlist = list(word_code) 
                    for i in incidice :
                        word_code_inlist[i] = char
                    word_code = ''.join(word_code_inlist) 
                    if "_" not in word_code :
                        print( "you complete it well done!!!")
                        guessed = True 



            if x==0  : 
                print(f" wrong{char} is wrong letter")
                tries -= 1 
                    
                print( display_hangman(tries))



        elif len(guess) == len(word) and guess.isalpha() :
            if guess == word :
                print(f"well done {guess} is the right word")
                guessed = True
            else : 
                print( f"no")
                print( display_hangman(tries))

        else : 
            print( " invalid input ")
    if guessed :
        print( " I tell you for the second time that you're amazing")




def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main () :
    word = get_word() 
    play(word)

while True :
    main()
    if input("do you wanna play again ? Y/N").upper() == "Y" :
        main()
    else : 
        break
