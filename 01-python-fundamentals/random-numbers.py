# Generate Random Numbers

import random

low = 1
high = 100
options = ('rock', 'paper', 'scissors')
cards = ['2', '3', '9', '7', '1', '5', '4']

# to get a random number
num = random.randint(low, high)

# to get a random float (<0)
num = random.random()

# slect from random options
option = random.choice(options)

# to shuffle numbers
random.shuffle(cards)

# Random Number Generator - Excercise 1
import random

# set range
low = 1
high = 10

# generate the random number
random_number = random.randint(low, high)

# get user input
user_input = 0

# compare users answer with user input
while user_input != random_number:
    user_input = int(input("Guess a number: "))

    if user_input == random_number:
        print("Correct!")
    else:
        print("Wrong! Try again.")

# Rock, Paper, Scissors Game - Excecise 2
import random

# set options
options = ['rock', 'paper', 'scissors']

# scores
player_score = 0
computer_score = 0

# game_status
game_status = True

# user name
user_name = input('Enter your name: ')

while game_status:
    # Users choice
    user_choice = input('Enter rock, paper or scissors (q to quit): ').strip().lower()
    # Computers choice
    computer_choice = random.choice(options)

    # logic for if they want to quit
    if  user_choice == 'q':
        game_status = False
        break

    # logic for cheching the current answers and handle scores
    if user_choice == computer_choice:
        print('Tie')
    elif user_choice == 'rock' and computer_choice == 'paper':
        print('Computer Wins')
        computer_score += 1
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print(f'{user_name} Wins')
        player_score += 1
    elif user_choice == 'paper' and computer_choice == 'rock':
        print(f'{user_name} Wins')
        player_score += 1
    elif user_choice == 'paper' and computer_choice == 'scissors':
        print('Computer Wins')
        computer_score += 1
    elif user_choice == 'scissors' and computer_choice == 'rock':
        print('Computer Wins')
        computer_score += 1
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print(f'{user_name} Wins')
        player_score += 1

    # display score
    print(f'Score: {user_name} {player_score} - {computer_score} Computer')

# Dice Roller Game - Excecise 3
import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input('How many dice?: '))

for die in range(num_of_dice):
  dice.append(random.randint(1,6))

for die in range (num_of_dice):
  for line in dice_art.get(dice[die]):
    print(line)

for die in dice:
  total += die
print(f'total: {total}')
