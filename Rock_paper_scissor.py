import random  # Import the random module for generating computer choices

# Dictionary to map each choice to its emoji
emojis = {'r': '🪨', 's': '✂️', 'p': '📃'}

# Tuple containing valid choices
choices = ('r', 'p', 's')

# Game loop runs until the user decides to exit
while True:
    # Ask the user for their choice and convert it to lowercase
    user_choice = input('Rock, Paper, or Scissors? (r/p/s): ').lower()

    # Validate user input
    if user_choice not in choices:
        print('Invalid Choice!')
        continue  # Ask again if input is invalid

    # Randomly select computer's choice
    computer_choice = random.choice(choices)

    # Display both choices with emojis
    print(f'You Choose {emojis[user_choice]}')
    print(f'Computer Choose {emojis[computer_choice]}')

    # Determine the outcome
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

    # Ask user if they want to play again
    should_continue = input('Continue? (y/n): ').lower()
    if should_continue == 'n':
        break  # Exit the game loop
