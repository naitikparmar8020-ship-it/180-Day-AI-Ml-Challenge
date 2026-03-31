#today's our task is to make a hangman project
#we will complete it by 5 step
#now it's time to create 1st step

#step 1 
#todo 1 randomly choose the word from the list and assign it into a variable called chosen_word.then print it
#todo 2 ask the user to guess a latter and assign thier answer into a varible called guess_word,make guess lower case
#todo 3 check if the latter the user guessed is one of the latter in the chosen_word print Right if it is right or Wrong if it is wrong

#step 2
#Todo 1 
#create an empty string called placeholder
#for each latter in chosen_word,add a _ to place holder
#so if the chosen word_was apple placeholder should be  _ _ _ _ _ 
#todo 2 now we add the latter which user inputs in that blanks

#step 3 
#todo 1 use a while loop to user let guess again
#todo 2 change the for loop so that you keep  the previous correct latter in the string

#step 4
#todo 1 create a variable called lives for taking keep records of the number of lives left 
#set lives equal to 6
#todo 2 if guess_word in not in chosen word, then reduce lives by 1 
#if lives  goes down to 0 then game should endand it's should print you lose
Stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |          
          
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |

=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |

=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |

=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |

=========''', '''
  +---+
  |   |
      |
      |
      |
      |

=========''']

word_list= ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

import random
# from hangman.Stages import Stagess
# from hangman.wordlist import word_list

lives=6
chosen_word=random.choice(word_list)
# print(chosen_word)

placeholder=""
for i in chosen_word:
    placeholder+="_"
    

print(placeholder)
correct_list=[]
game_over=False
while not game_over:
    print(f"*****************************************{lives}/6 lives remaning****************************************************")
    guess_word=input("Guess a latter for hangman:-").lower()
    if guess_word in correct_list: 
         print("you alredy used this latter")
    else:
        display=""
        for i in guess_word:
                if guess_word not in chosen_word:
                    lives-=1
                    print(f"you guess a {guess_word} latter which is not in word. Lose life")
        for i in chosen_word:
            if guess_word==i:  
                    display+=i
                    correct_list.append(guess_word)
            elif i in correct_list:
                display+=i
            else:
                display+="_"

        print(display)
        print(lives)
        if "_" not in display:
            game_over=True
            print("*********************************YOU WON*******************************************")
        elif lives==0:
            game_over=True
            print(f"*********************************YOU LOSE*******************************************")
            print(f"the correct word is {chosen_word}")
        print(Stages[lives])


"""
for i in chosen_word:
    if guess_word == i:
        print("Right")
    else:
        print("Wrong")
"""