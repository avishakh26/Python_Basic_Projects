import random  # This module allows us to generate random choices, like picking a word for the game.
from datetime import datetime  # This module helps us record the date and time when a match is played.

# Function to save match history to a text file
def save_match_history_to_file(player1, player2, winner, word, incorrect_guesses):
    # Open the file "hangman_history.txt" in append mode to add new data to the file
    with open("hangman_history.txt", "a") as file:
        # Prepare the match details as a string, including the date, players, winner, word, and incorrect guesses.
        match_data = f"Date: {datetime.now()} | Player 1: {player1} | Player 2: {player2} | Winner: {winner} | Word: {word} | Incorrect Guesses: {incorrect_guesses}\n"
        # Write the match details to the file
        file.write(match_data)

# Function to get a random word from a predefined list of words
def get_random_word():
    # List of possible words for the game
    word_list = ["aardvark", "baboon", "camel", "jazz", "grass", "follow", "castle", "cloud"]
    # Randomly choose a word from the list and return it
    return random.choice(word_list)

# Function to process the player's guess and check if it's correct
def making_a_guess(guess, chosen_word, blank_list):
    correct_guess = False  # Start by assuming the guess is incorrect
    # Check each letter of the chosen word to see if it matches the player's guess
    for x in range(len(chosen_word)):
        # If the guess is correct and matches a letter in the word, update the blank list
        if guess.lower() == chosen_word[x]:
            blank_list[x] = guess.lower()  # Fill in the guessed letter in the correct position
            correct_guess = True  # The guess was correct, so we update this to True
    return correct_guess  # Return whether the guess was correct or not

# Function to print the hangman visuals (the drawing of the hangman)
def print_hangman(update_display):
    # A list of possible hangman images for each stage of the game (from 0 to 6 incorrect guesses)
    HANGMANPICS = ['''+---+
  |   |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    # Print the hangman image corresponding to the current incorrect guess count
    print(HANGMANPICS[update_display])

# Main function that runs the game between two players
def play_game(player1, player2):
    # Get a random word for the game
    chosen_word = get_random_word()
    # Create a list of blanks (underscores) to represent the word
    blank_list = ["_"] * len(chosen_word)
    update_display = 0  # Variable to track how many incorrect guesses have been made
    incorrect_guesses = 0  # Counter for incorrect guesses
    current_player = player1  # Start with player1

    # Greet the players and inform them that the word has been chosen
    print(f"Welcome to Hangman, {player1} and {player2}!")
    print("The word has been chosen.")
    # Show the blank word (initially with underscores for each letter)
    print(" ".join(blank_list))

    # Game loop: keeps running until there are 6 incorrect guesses (game over) or the word is guessed
    while update_display < 6:
        # Ask the current player to make a guess (a single letter)
        guess = input(f"{current_player}, make a guess (single letter): ").lower()

        # Check if the input is valid (only one letter and an alphabet letter)
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")  # If the input is invalid, ask again
            continue

        # Call the function to process the guess and check if it's correct
        correct_guess = making_a_guess(guess, chosen_word, blank_list)

        # If the guess was correct, show the updated word with the new correct letter
        if correct_guess:
            print(f"Good guess! The word now looks like this: {''.join(blank_list)}")
        else:
            # If the guess was incorrect, increase the incorrect guess count and print the hangman visual
            print(f"There is no {guess}. Sorry.")
            update_display += 1  # Increment the incorrect guess count
            incorrect_guesses += 1  # Count the incorrect guess
            print_hangman(update_display)  # Show the hangman drawing

        # Check if the word has been completely guessed
        if "".join(blank_list) == chosen_word:
            # If the word is fully guessed, announce the winner and save the match history
            print(f"Congratulations, {current_player}! You guessed the word: {chosen_word}")
            winner = current_player
            save_match_history_to_file(player1, player2, winner, chosen_word, incorrect_guesses)
            break  # End the game since someone has won
        else:
            # If the word isn't guessed yet, show the current state of the word (with blanks and correct letters)
            print(" ".join(blank_list))

        # Switch players: if it's player1's turn, now it's player2's turn, and vice versa
        current_player = player2 if current_player == player1 else player1

    # If there are 6 incorrect guesses, the game is over and no one won
    if update_display == 6:
        print("GAME OVER. The word was:", chosen_word)
        winner = "No one"  # No winner if the game ends with 6 incorrect guesses
        save_match_history_to_file(player1, player2, winner, chosen_word, incorrect_guesses)

# Function to start the game by getting players' names and calling the main game function
def start_game():
    # Ask for the names of the two players
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")
    # Start the game with the provided player names
    play_game(player1, player2)

# Run the game by calling the start_game function
start_game()



