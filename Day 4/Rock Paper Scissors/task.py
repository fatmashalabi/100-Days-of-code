import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = [rock, paper, scissors]
player_index= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if(player_index < 0 or player_index>2):
    print("Invalid number, You lose!")
else:
 player_choice = list[player_index]
 print("Your choice:" + player_choice)
 random_index = random.randint(0, 2)
 computer_choice = list[random_index]
 print("Computer choice: " + computer_choice)
 if(player_choice == computer_choice):
    print("It's a draw!")
 elif((player_choice == rock and computer_choice == scissors) or (player_choice == paper and computer_choice == rock) or (player_choice ==scissors and computer_choice ==paper)):
    print("You win!")
 else:
    print("You lose!")
