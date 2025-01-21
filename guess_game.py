import random


def generate_number(difficulty):
    """Generates a random number between 0 and the specified difficulty
    saving it as the secret_number"""
    secret_number = random.randint(0, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    """Prompts the user to input a number within the range of 0 to the
        difficulty and returns the entered number."""
    guess = input("Please enter your guess number between 0 and the difficulty level:\n")
    from utils import validate_number
    validated_guess = validate_number(guess, [0, difficulty])
    return validated_guess


def compare_results(secret_number, user_guess):
    """Compares the generated secret number with the user's input and
        determines if they match."""
    return secret_number == user_guess


def play(difficulty):
    """Initiates the game by calling the functions above and returns True if the user wins, and
    False if the user loses."""
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    return compare_results(secret_number, user_guess)
