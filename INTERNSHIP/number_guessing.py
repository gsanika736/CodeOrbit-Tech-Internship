
# ==========================================
# NUMBER GUESSING GAME
# ==========================================

# Importing random module to generate random numbers
import random


# Function to play one round of the game
def play_game():

    # Computer selects a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Initialize the attempt counter
    attempts = 0

    print("\n====================================")
    print("       NUMBER GUESSING GAME")
    print("====================================")
    print("I have selected a number between 1 and 100.")
    print("Try to guess the correct number!")

    # Loop continues until the correct guess
    while True:

        try:
            # Take input from the user
            guess = int(input("\nEnter your guess: "))

            # Check whether the number is within range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            # Increase the attempt counter
            attempts += 1

            # Compare user's guess with the secret number
            if guess < secret_number:
                print("Too Low! Try a higher number.")

            elif guess > secret_number:
                print("Too High! Try a lower number.")

            else:
                print("\nCongratulations! You guessed the correct number!")
                print("The secret number was:", secret_number)
                print("Total attempts taken:", attempts)
                break

        # Handle invalid input
        except ValueError:
            print("Invalid input! Please enter a whole number.")


# Main loop to allow multiple rounds
while True:

    # Start a new game
    play_game()

    # Ask the user whether they want to play again
    play_again = input(
        "\nDo you want to play another round? (yes/no): "
    ).lower().strip()

    # Exit the game if the user says no
    if play_again != "yes":
        print("\nThank you for playing!")
        print("Game closed successfully.")
        break
