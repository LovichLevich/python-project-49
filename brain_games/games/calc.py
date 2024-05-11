import random

RAND_NUMBER_MIN = 1
RAND_NUMBER_MIDDLE = 50
RAND_NUMBER_MAX = 100

QUESTIONS = 'What is the result of the expression?'


def create_numbers_in_question():
    rand_num_1 = random.randint(RAND_NUMBER_MIDDLE, RAND_NUMBER_MAX)
    rand_num_2 = random.randint(RAND_NUMBER_MIN, RAND_NUMBER_MIDDLE)
    symbols = random.choice('+-*')
    number = f'{rand_num_1} {symbols} {rand_num_2}'
    correct_answer = str(evaluate(rand_num_1, symbols, rand_num_2))
    return number, correct_answer


def evaluate(num_1, symbol, num_2):
    if symbol == '+':
        return num_1 + num_2
    elif symbol == '-':
        return num_1 - num_2
    else:
        return num_1 * num_2
