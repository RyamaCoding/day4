# ROCK PAPER SCISSORS GAME

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

game_images = [rock, paper, scissors]
random_choice = random.choice(game_images)

print("Welcome to the Rock, Paper, Scissors Game!")

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors")

if player_choice == "0":
    print(f"Player chose:\nRock\n{rock}")
elif player_choice == "1":
    print(f"Player chose:\nPaper\n{paper}")
elif player_choice == "2": 
    print(f"Player chose:\nScissors\n{scissors}")
else: 
    print("Invalid choice")

if random_choice == rock:
    random_choice_name = "Rock"
elif random_choice == paper:
    random_choice_name = "Paper"
else:
    random_choice_name = "Scissors"

print(f"Computer chose:\n{random_choice_name}\n{random_choice}")

if (player_choice == 0 and random_choice == rock) or (player_choice == "1" and random_choice == paper) or (player_choice == "2" and random_choice == scissors): 
    print("It's a tie!")
elif (player_choice == "0" and random_choice == scissors) or (player_choice == "1" and random_choice == rock) or (player_choice == "2" and random_choice == paper):
    print("You win!")
else:
    print("You lose!")






