

import time  # Importing the time module to track time


class TreasureIsland:
    def __init__(self):
        """Initialize the game with default settings."""
        self.treasure_location = (3, 4)  # Coordinates where the treasure is located on the grid.
        self.map_size = (5, 5)  # The grid size, here it's 5x5.
        self.guess_limit = 5  # Maximum number of guesses the player can make.
        self.guesses_left = self.guess_limit  # Initialize the number of guesses remaining.
        self.start_time = time.time()  # Record the start time for the time limit.


    def display_map(self):
        """Display the current game map with the treasure location."""
        for row in range(self.map_size[0]):  # Loop over each row in the grid
            for col in range(self.map_size[1]):  # Loop over each column in the grid
                if (row, col) == self.treasure_location:  # Check if current position is the treasure
                    print("X", end=" ")  # Mark treasure with 'X'
                else:
                    print("O", end=" ")  # Mark other locations with 'O'
            print()  # Move to the next line after each row



    def check_location(self, guess):
        """Check if the player's guess is correct."""
        if guess == self.treasure_location:  # If the guess matches the treasure location
            return "Congratulations! You've found the treasure!"  # Return success message
        else:
            return "Sorry, no treasure here."  # Return failure message if guess is incorrect



    def give_hint(self, guess):
        """Give a hint about the treasure location based on the player's guess."""
        if guess[0] < self.treasure_location[0]:  # If the guessed row is below the treasure row
            return "The treasure is lower in row."
        elif guess[0] > self.treasure_location[0]:  # If the guessed row is above the treasure row
            return "The treasure is higher in row."
        elif guess[1] < self.treasure_location[1]:  # If the guessed column is to the left of the treasure column
            return "The treasure is to the right in column."
        elif guess[1] > self.treasure_location[1]:  # If the guessed column is to the right of the treasure column
            return "The treasure is to the left in column."
        return "You are very close! But still not at the right spot."  # If the guess is near but not exact




    def decrement_guesses(self):
        """Decrement the number of guesses left."""
        self.guesses_left -= 1  # Subtract 1 from the number of guesses left



    def has_guesses_left(self):
        """Check if the player has guesses left."""
        return self.guesses_left > 0  # Return True if guesses are remaining, otherwise False



    def time_left(self):
        """Check if the game time has expired."""
        elapsed_time = time.time() - self.start_time  # Calculate the time that has passed since the game started
        return 30 - elapsed_time  # Return the remaining time in seconds (30 seconds - elapsed time)



    def is_guess_valid(self, guess):
        """Check if the guess is within the allowed grid range."""
        return 0 <= guess[0] < self.map_size[0] and 0 <= guess[1] < self.map_size[1]  # Check if the guess is valid (within grid size)


if __name__ == "__main__":
    island = TreasureIsland()  # Initialize the game instance



    while island.has_guesses_left():  # Continue while the player has guesses remaining
        remaining_time = island.time_left()  # Calculate the remaining time for the game
        
        
        if remaining_time <= 0:  # If time has run out
            print("Time's up! You didn't find the treasure in time.")  # Notify the player
            print("Game over! The treasure was at:", island.treasure_location)  # Reveal the treasure's location
            break  # End the game


        island.display_map()  # Display the game map showing 'O' for empty spots and 'X' for the treasure
        print(f"Guesses left: {island.guesses_left}")  # Print the number of guesses left
        print(f"Time left: {int(remaining_time)} seconds")  # Print the remaining time (rounded to nearest second)



        try:
            # Prompt the player to enter a guess for the row and column
            user_guess = (int(input("Enter row (0-4): ")), int(input("Enter column (0-4): ")))
            
            
            
            if not island.is_guess_valid(user_guess):  # Check if the guess is valid
                print("Invalid guess! Please enter values between 0 and 4 for both row and column.")  # If invalid, prompt again
                continue  # Skip the rest of the loop and ask for input again
        except ValueError:  # Handle cases where the input is not an integer
            print("Invalid input! Please enter valid integer values.")  # Notify the user about the invalid input
            continue  # Skip the rest of the loop and ask for input again



        result = island.check_location(user_guess)  # Check if the guess is correct
        print(result)  # Print the result (success or failure)



        if result == "Sorry, no treasure here.":  # If the guess is incorrect
            print("Hint:", island.give_hint(user_guess))  # Offer a hint to guide the player
            island.decrement_guesses()  # Decrease the number of guesses left.



        if not island.has_guesses_left():  # If the player has no guesses left
            print("Game over! The treasure was at:", island.treasure_location)  # Reveal the treasure's location
            break  # End the game


