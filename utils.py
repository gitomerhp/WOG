SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 1


def validate_number(number, number_range):
    """validates the number is a digit and within the specified range"""
    while True:
        # validate numbers
        if not number.isdigit():
            number = input('Please enter an actual number\n')
            continue
        # validate range
        elif number_range[1] == -1:
            #  must be larger than first number in range
            if int(number) <= number_range[0]:
                number = input(f'The number must be larger than {number_range[0]}\n')
                continue
            else:
                return int(number)
        # must be between two numbers
        elif int(number) not in range(number_range[0], number_range[1]+1):
            number = input(f'The number must be from {number_range[0]} to {number_range[1]}\n')
            continue
        else:
            return int(number)


def screen_cleaner():
    """Clears the screen"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
