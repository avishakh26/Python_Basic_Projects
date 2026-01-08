

import random
import time


print('''
+++=====|||| Welcome To GTNGO have fun ||||=====+++

"Guess a number within 1 to 30"
''')

# Generate a random number between 1 and 30
num = random.randint(1, 30)

# Number of players
num_players = int(input("Enter number of players: "))

# Store player names
players = []
for i in range(num_players):
    player_name = input(f"Enter the name of player {i + 1}: ")
    players.append(player_name)

# Maximum number of attempts per player
max_attempts = 5
# Time limit for each guess (in seconds)
time_limit = 15

# Track the game state
current_turn = 0  # Start with the first player
attempts_left = [max_attempts] * num_players  # List to track remaining attempts for each player

print(f"\nWelcome {', '.join(players)}! Let's start the game!")
print(f"Each player has {max_attempts} attempts to guess the correct number. You have {time_limit} seconds per guess.")

# Game loop
while True:
    current_player = players[current_turn]
    print(f"\n{current_player}'s turn")

    for attempt in range(1, attempts_left[current_turn] + 1):
        print(f"Attempt {attempt}/{max_attempts} - {current_player}, you have {time_limit} seconds to guess.")
        
        # Start timing the player's guess
        start_time = time.time()

        # Get player's guess with time limit
        try:
            # Allow the player to enter their guess within the time limit
            inputnumber = None
            while time.time() - start_time < time_limit:
                guess_input = input(f"Enter your number: ")
                if guess_input:
                    inputnumber = int(guess_input)
                    if 1 <= inputnumber <= 30:
                        break
                    else:
                        print("Please guess a number between 1 and 30.")
                else:
                    print("No input detected yet. Keep guessing.")

            # If time exceeds limit
            if time.time() - start_time >= time_limit:
                print(f"Time's up! {current_player}, you took too long to guess.")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        # Check if the guess is correct
        if inputnumber > num:
            print("Your Input Number is too big!")
        elif inputnumber < num:
            print("Your Input Number is too small!")
        else:
            print(f"Congratulations, {current_player}! You guessed the right number: {num}. Great job!")
            break
    else:
        print(f"Sorry, {current_player}, you've used all your attempts.")

    # Check if the game is over
    if inputnumber == num:
        print(f"\n{current_player} wins the game!")
        break
    
    

    # Move to the next player
    current_turn = (current_turn + 1) % num_players

    # Check if all players have used their attempts
    if all(attempts == 0 for attempts in attempts_left):
        print(f"\nNo one guessed the correct number. The correct number was {num}.")
        break


