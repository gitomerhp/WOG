"""
A package that is in charge of managing the scores file. The scores file at this point will consist of
only a number. That number is the accumulation of the winnings of the user. Amount of points for
winning a game is as follows: POINTS_OF_WINNING = (DIFFICULTY X 3) + 5 Each time the user is
winning a game, the points he one will be added to his current amount of point saved in a file.
"""


def add_score(difficulty):
    """The function will try to read the current score in the scores file,
    if it fails it will create a new one and will use it to save the current score."""
    current_score = (difficulty * 3) + 5
    try:
        with open('scores.txt', 'r') as file:
            previous_score = int(file.read())
    except FileNotFoundError:
        previous_score = 0
    new_score = current_score + previous_score
    print(f'Your previous score was: {previous_score}')  # debug
    print(f'The current score for this game is: {current_score}')  # debug
    print(f'Your total new score is: {new_score}\n')  # debug
    with open('scores.txt', 'w') as file:
        file.write(str(new_score))
