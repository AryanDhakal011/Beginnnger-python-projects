# Rock, paper , scissors logic with random 
import random 

user_chocie = int(input("enter your choice \n 1 for rock \n 2 for scissors \n 3 for paper "))
num_generate = random.randint(1, 3)

rock_draw =("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper_draw = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors_draw = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

if user_chocie == 1 and num_generate == 1 : 
   print(rock_draw)
   print("Computer played rock")
   print(rock_draw)
   print("You draw")
elif user_chocie == 2 and num_generate == 1 : 
   print(rock_draw)
   print("Computer played rock")
   print(scissors_draw)
   print("You lose, rock beats scissors")
elif user_chocie == 3 and num_generate == 1: 
   print(rock_draw)
   print("Computer played rock")
   print(paper_draw)
   print("You win, paper beats rock")
   
   
elif user_chocie == 1 and num_generate == 2 :
   print(scissors_draw)
   print("Computer played scissors")
   print(rock_draw)
   print("You win, rock beats scissors")
elif user_chocie == 2 and num_generate == 2 : 
   print(scissors_draw)
   print("Computer played scissors")
   print(scissors_draw)
   print('You draw')
elif user_chocie == 3 and num_generate == 2 : 
   print(scissors_draw)
   print("Computer played scissors")
   print(paper_draw)
   print("You lose , scissors beats paper")


elif user_chocie == 1 and num_generate == 3: 
   print(paper_draw)
   print("Computer played scissors")
   print(rock_draw)
   print("You lose , paper beats rock")
elif user_chocie == 2 and num_generate == 3: 
   print(paper_draw)
   print("Computer played scissors")
   print(scissors_draw)
   print("You win , scissors beats paper ")
elif user_chocie == 3 and num_generate == 3:
   print(paper_draw)
   print("Computer played scissors")
   print(paper_draw)
   print("You draw")
else:
   print("Invalid number(type from your range")