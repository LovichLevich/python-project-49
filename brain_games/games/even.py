from random import randint

RAND_NUMBER_MIN = 1
RAND_NUMBER_MAX = 100

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def create_numbers_in_question():
    game_question = randint(RAND_NUMBER_MIN, RAND_NUMBER_MAX)
    correct_answer = 'yes' if is_even(game_question) else 'no'
    return game_question, correct_answer
