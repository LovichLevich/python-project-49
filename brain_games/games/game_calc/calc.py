import random

RAND_NUMBER_MIN = 1
RAND_NUMBER_MIDDLE = 50
RAND_NUMBER_MAX = 100

questions = 'What is the result of the expression?'


def number_in_questions():
    rand_num_1 = random.randint(RAND_NUMBER_MIDDLE, RAND_NUMBER_MAX)
    rand_num_2 = random.randint(RAND_NUMBER_MIN, RAND_NUMBER_MIDDLE)
    symbols = random.choice('+-*')
    number = f'{rand_num_1} {symbols} {rand_num_2}'
    correct_answer = str(eval(f'{rand_num_1} {symbols} {rand_num_2}'))
    return number, correct_answer
