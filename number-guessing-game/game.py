import random

def number_guessing_game():
    """
    A number guessing game where the user tries to guess a random number.
    """
    print("Welcome to the Number Guessing Game!")
    
    # Get player's name
    player_name = input("What's your name? ")
    print(f"Hello, {player_name}! I'm thinking of a number between 1 and 100.")

    # Generate a random number
    secret_number = random.randint(1, 100)
    
    # Set the number of attempts
    max_attempts = 10
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too Low!")
        elif guess > secret_number:
            print("Too High!")
        else:
            print(f"Congratulations, {player_name}! You guessed the number in {attempts} attempts.")
            return

    print(f"Sorry, {player_name}, you've run out of attempts. The number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
