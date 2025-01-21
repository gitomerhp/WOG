import random
from currency_converter import CurrencyConverter


def generate_number():
    """Generates a random number between 0 and the specified difficulty
    saving it as the secret_number"""
    random_number = random.randint(1, 100)
    return random_number


def get_money_interval(difficulty, generated_number):
    """Retrieves the current USD to ILS exchange rate and calculates an
    interval for the correct answer based on the game's difficulty level."""
    # get rate
    currency_rates = CurrencyConverter()
    rate = round(currency_rates.convert(1, 'USD', 'ILS'), 2)

    # get difficulty
    diff = 10 - difficulty
    diff_interval = [-diff, diff]

    # get interval
    actual_value = rate * generated_number
    final_diff = [round(actual_value + diff_interval[0], 2),
                  round(actual_value + diff_interval[1], 2)]
    return final_diff


def get_guess_from_user(generated_number):
    """Prompts the user to input a guess for the converted value of a
    specified amount in USD."""
    from utils import validate_number
    guess = input(f"Please enter your guess for {generated_number}$ in ILS:\n")
    guess = validate_number(guess, [0, -1])
    return guess


def compare_results(difficulty):
    """Executes the game by employing the functions above, and returns True if
    the user wins, and False if the user loses."""
    generated_number = generate_number()
    guess = get_guess_from_user(generated_number)
    interval = get_money_interval(difficulty, generated_number)
    print(f'actual value is: {interval[0]+(10-difficulty)} and your guess was: {guess}')
    if interval[0] <= guess <= interval[1]:
        return True
    else:
        return False


def play(difficulty):
    """Executes the game by invoking the functions above and returns True if the user wins,
    and False if the user loses."""
    return compare_results(difficulty)
