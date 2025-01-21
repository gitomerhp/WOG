import random
import time


def generate_sequence(difficulty):
    """Generates a list of random numbers between 1 and 101, with a length
        equal to the difficulty"""
    seq = []
    for i in range(0, difficulty):
        new_number = random.randint(1, 101)
        seq.append(new_number)
    return seq


def get_list_from_user(difficulty):
    """ Prompts the user to input a list of numbers matching the length of the
        generated sequence."""
    seq = []
    from app import validate_number
    for i in range(0, difficulty):
        new_number = input('Please enter a number:\n')
        new_number = validate_number(new_number, [1, 101])
        seq.append(new_number)
    return seq


def is_list_equal(seq1, seq2):
    """ Compares two lists to verify if they are identical, returning True if they match
        and False otherwise."""
    return seq1 == seq2


def show_sequence(sequence, display_time):
    """Display a sequence of numbers briefly, then clear the screen."""
    input('Press any key when you are ready to see and memorize the sequence:\n')
    # Show the sequence
    print(sequence)
    # Wait for the specified time
    time.sleep(display_time)
    # Clear the screen
    from utils import screen_cleaner
    screen_cleaner()


def play(difficulty):
    """Executes the game by invoking the functions above and returns True if the user wins,
    and False if the user loses."""

    # generate sequence
    generated_seq = generate_sequence(difficulty)

    # show the sequence for x seconds
    show_sequence(generated_seq, 0.7)

    # get user sequence
    user_seq = get_list_from_user(difficulty)

    # compare sequences and print result
    return is_list_equal(generated_seq, user_seq)
