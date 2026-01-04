


class TreasureIsland:
    def __init__(self):
        self.treasure_location = (3, 4)  # Adjusted to a valid coordinate
        self.map_size = (5, 5)
        self.guess_limit = 5  # Max number of guesses allowed
        self.guesses_left = self.guess_limit



    def display_map(self):
        for row in range(self.map_size[0]):
            for col in range(self.map_size[1]):
                if (row, col) == self.treasure_location:
                    print("X", end=" ")  # Mark treasure with 'X'
                else:
                    print("O", end=" ")  # Mark other locations with 'O'
            print()
            
            
            

    def check_location(self, guess):
        """Check if the player's guess is correct."""
        if guess == self.treasure_location:
            return "Congratulations! You've found the treasure!"
        else:
            return "Sorry, no treasure here."



    def give_hint(self, guess):
        """Give a hint about the treasure location."""
        if guess[0] < self.treasure_location[0]:
            return "The treasure is lower in row."
        elif guess[0] > self.treasure_location[0]:
            return "The treasure is higher in row."
        elif guess[1] < self.treasure_location[1]:
            return "The treasure is to the right in column."
        elif guess[1] > self.treasure_location[1]:
            return "The treasure is to the left in column."
        return "You are very close! But still not at the right spot."




    def decrement_guesses(self):
        """Decrement the number of guesses left."""
        self.guesses_left -= 1



    def has_guesses_left(self):
        """Check if the player has guesses left."""
        return self.guesses_left > 0



if __name__ == "__main__":
    island = TreasureIsland()



    while island.has_guesses_left():
        island.display_map()  # Display the map with 'O's and 'X' at the treasure location
        print(f"Guesses left: {island.guesses_left}")
        
        # User input for guessing the location
        user_guess = (int(input("Enter row (0-4): ")), int(input("Enter column (0-4): ")))

        # Check if the guess is correct
        result = island.check_location(user_guess)
        print(result)



        if result == "Sorry, no treasure here.":
            # Offer a hint
            print("Hint:", island.give_hint(user_guess))
            island.decrement_guesses()

        # End the game if the player has no guesses left
        if not island.has_guesses_left():
            print("Game over! The treasure was at:", island.treasure_location)
            break





