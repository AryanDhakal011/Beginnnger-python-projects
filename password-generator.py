#Hard lesson , password generator(There is easy level and hard level)

import random 

print("Welcome to the password generator")

#remember to keep all items in the list under quotations

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1','2','3','4','5','6','7','8','9','10']
symbols = ['!', '@', '#', '$', '*']


nr_letters = int(input("How many letters would you like in your password \n"))

nr_symbols = int(input(f"How many symbols would you like? \n"))

nr_numbers  = int(input(f"How many numbers would you like \n"))

#Eazy level 
# fghf^@23 is a random passoword with a pattern of alphabet symbols and numbers 
#basic rundown : you hava a password generator where you store random letters, symbols and numbers in a list. then you ask the user how many letters, symbols and numbers do they want in their randomly generated password.For that

#first you need a variable password 

password ="" 

#then using for loop set the number of letters the user will ask , random.choice is used for selecting random item from the list.

for char in range (1,nr_letters+ 1 ): 
    password = password + random.choice(letters)

for char in range(1, nr_symbols +1 ): 
    password = password + random.choice(symbols)

for char in range(1, nr_numbers +1 ): 
    password = password + random.choice(numbers)
    
print(password)

#hard level generate password that is different everytime like g#678hs@j2@
 #first create a password list so that you can add each letters and symbols in the list
  
password_list =[]

#append() method takes an object as an argument and adds it to the end of an existing list.

for char in range (1,nr_letters+ 1 ): 
    password_list.append( random.choice(letters))

for char in range(1, nr_symbols +1 ): 
    password_list.append(random.choice(symbols))

for char in range(1, nr_numbers +1 ): 
    password_list.append(  random.choice(numbers))
#to mix up the items in a list you use random.shuffle(list)
print(password_list)

random.shuffle(password_list)

print(password_list)

#now to turn it back into a string as it is in quotations and inside a bracket
#create password var,(its creted again)
password ="" 
for char in password_list: 
    password += char #adding all the items into var password
    
print(f"Your password is {password}")