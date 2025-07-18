#Ask the user to make a choice
#if the choice is not valid
#  print an error
#let the computer to make a choice
#print choices (emojis)
#determine the winner
#ask the user if they want to continue
#if not
#  terminate

import random

emojis = {'r':'🪨', 's':'✂️','p':'📃'}
choices = ('r','p','s')

while True:
    user_choice = input('Rock, Paper, or Scissors? (r/p/s):').lower()
    if user_choice not in choices:
        print('Invalid Choice!')
        continue

    computer_choice = random.choice(choices)
    print(f'You Choose {emojis[user_choice]}')
    print(f'Computer Choose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('Tie!')
    elif user_choice == 'r' and computer_choice == 's':
        print('You win')
    elif user_choice == 's' and computer_choice == 'p':
        print('You win')
    elif user_choice == 'p' and computer_choice == 'r':
        print('You Win')
    else:
        print('You Lose!')

    should_continue = input('Continue? (y/n): ').lower()
    if should_continue == 'n':
        break
