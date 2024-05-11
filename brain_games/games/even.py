from random import randint

RAND_NUMBER_MIN = 1
RAND_NUMBER_MAX = 100

QUESTIONS = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def create_numbers_in_question():
    number = randint(RAND_NUMBER_MIN, RAND_NUMBER_MAX)
    correct_answer = 'yes' if is_even(number) else 'no'
    return number, correct_answer
