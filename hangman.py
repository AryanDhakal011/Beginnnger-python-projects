#Hangman-DIFFICULT CHALLANGE: 
#THIS IS A DIFFICULT CHALLANGE AND MODULES TO KEEP THE FILES SUCH AS HANGMAN-ART IS NOT USED TO SHOW THE FULL CODE BUT IT CAN BE USED USING From (file-name) import (variable-name)

import random 
#stages drawings are in descending order so all we have to do is simply print the stages and corresponding to the current number of lives(remember how lists work)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)#just printing logo to make it more attractive 

#given word list
word_list = ["aardvark", "baboon", "camel"] 
                     
lives = 6
end_of_game = False #we created a limit boolean condition to end game after completion of the word

display = []
chosen_word = random.choice(word_list)
#chooses a random word from the list
for letter in chosen_word: #we let a variable "letter" in list chosen_word and made it display '_' to replace the letters for eg apple = _ _ _ _ _ 
    display += '_'

testing = print(f"pss the answer is {chosen_word}")
print(testing)#prints out the chosen word for testing

while not end_of_game: #using whle loop,while end of game is not true do this again
    guess = input("Enter your guess \n").lower() # make user guess a word 
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(len (chosen_word)): #we took variable position, then used position of a word for eg apple =01234 in positiion so
        letter = chosen_word[position]#this line becomes letter = appple(0)..runs in loop till 4 
        if letter == guess: #this line says if letter that is 'a' is equal to the guessed letter that user entered ,do below
            display[position] = letter# display meant '_' first now its _[0] = letter(which is 'a')
        
    if guess not in chosen_word:
        print(f"You've guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1        
        if lives == 0: 
            end_of_game = True 
            print("you lose")
            print(f"The correct word was {chosen_word}")

    print(display)#printing the display 
    
    if '_' not in display:#In this loop we are telling if there is no more empty spaces '_' left , end_of_game becomes true and while loop's condition ends.
        end_of_game = True 
        print ("you win")

    print(stages[lives])

#Example of using function to find out how many cans you need to paint a wall:
import math 
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5 


def paint_calc(height , width, cover):
    total = (height * width) / cover
    total_round = math.ceil(total)
    print(f"You have to buy {total_round} cans of paint")
paint_calc(test_h,test_w,coverage)

#using function find if a number is prime or not

def prime_checker(number): 
    is_prime = True 
    for i in range(2,number):
        if number % i == 0:
            is_prime = False 
    if is_prime:
        print("it is a prime number")
    else:
        print("it is not a prime number")
        
prime_checker(1)

# MAKING an encoding and decoding program:

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e',
 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#first we need 3 inputs to ask the user, to encode or decode then the to enter the text , and finally how many letters they want to shift.
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#Method 1 with defining 2 functions encrypt decrypt and using if else for determining which is used
def encrypt(text_input,shift_input): 
    cipher_text = "" # we create an empty variable for output 
    for letter in text_input:# running for loop for input text
        position = alphabet.index(letter) # we determine the position of each letter using .index function
        new_position = position + shift_input # we calculate the new position of the letter
        new_letter = alphabet[new_position] #then the new letter will be the shifted position in the alphabet list
        cipher_text += new_letter #store it in a new variable 
    print(f"The encoded text is {cipher_text}")


encrypt(text_input = text, shift_input = shift)# call the function

def decrypt(cipher_text, shift_input):# same thing with decrypt but we use cipher_text instead of text input since its already taken 
    plain_text = "" # create an empty variable 
    for letter in cipher_text:# running for loop for each letter in cipher_text(the output from encoding)
        position = alphabet.index(letter)#determing the position same as above 
        new_position = position - shift_input # creating new position since we have to go back we subtract the amount 
        plain_text += alphabet[new_position] #it will be shifted in new position 
    print(f"the decoded text is {plain_text}")#printing the new text
    
#use if and else for determining encoding and decoding 
if direction == "encode":
    encrypt(text_input=text, shift_input=shift)
elif direction == "decode": 
    decrypt(cipher_text =text,shift_input=shift)
    
    
#direct method
def caesar(start_text, shift_input, cipher_diretion):# create 3 variables ,to start text, the shift amount and in the end the cipher direction 
    end_text = "" #empty variable 
    if cipher_diretion == "decode": #if decode, we multiply by - ,which makes 1 = -1 , 2 = -2 and so on dont use this line in for loop or else it will multiply -1 over and over and wrong input is displayed
        
        shift_input *= -1 
    for letter in start_text:# run for loop for entered text
        position = alphabet.index(letter) # determine the position using index
        
        new_position = position + shift_input # new position is determined with position for eg = 1 and entered shift amount = 5 so total = 6 
        end_text += alphabet[new_position]# end text variable is used which was empty and alphabet is added to it.
    print(f"the {cipher_diretion}text is{end_text}")# finally it is printed ,to determine encode or decode we use cipher_direction variable
    
caesar(start_text=text ,shift_input=shift, cipher_diretion=direction) # calling the function