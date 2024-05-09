from random import randint

RAND_NUMBER_MIN = 1
RAND_NUMBER_MAX = 100

questions = 'Answer "yes" if the number is even, otherwise answer "no".'


def answer_in_questions(number):
    return number % 2 == 0


def number_in_questions():
    number = randint(RAND_NUMBER_MIN, RAND_NUMBER_MAX)
    correct_answer = 'yes' if answer_in_questions(number) else 'no'
    return number, correct_answer
