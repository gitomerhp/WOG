from utils import validate_number
from guess_game import play as guess_play
from memory_game import play as memory_play
from currency_roulette_game import play as currency_play
from score import add_score


def welcome():
    username = input('please insert your name:\n')
    print(f'Hi {username} and welcome to the World of Games: The Epic Journey')


def start_play():
    while True:
        # get game type
        game_type = input('''Please choose a game to play:
            1. Memory Game - a sequence of numbers will appear for 1 second and you have to
            guess it back.
            2. Guess Game - guess a number and see if you chose like the computer.
            3. Currency Roulette - try and guess the value of a random amount of USD in ILS
            4. Exit\n''')
        game_type = validate_number(game_type, [1, 4])

        # exit game
        if game_type == 4:
            print('Goodbye')
            break

        # get difficulty level
        diffculty_level = input('Please choose game difficulty from 1 to 5:\n')
        difficulty = validate_number(diffculty_level, [1, 5])

        games = ['Memory Game', 'Guess Game', 'Currency Roulette']
        print(f'\nPlaying: {games[game_type-1]} on difficulty level: {difficulty}\n')

        won = False
        # start specific game
        if game_type == 1:
            won = memory_play(difficulty)
        elif game_type == 2:
            won = guess_play(difficulty)
        elif game_type == 3:
            won = currency_play(difficulty)
        if won:
            add_score(difficulty)
