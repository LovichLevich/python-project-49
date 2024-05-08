import random

RAND_NUMBER_MIN = 1
RANF_NUMBER_MIDLE = 50
RAND_NUMBER_MAX = 100

questions = 'What is the result of the expression?'

def number_in_questions():
    rand_num_1 = random.randint(RANF_NUMBER_MIDLE, RAND_NUMBER_MAX)
    rand_num_2 = random.randint(RAND_NUMBER_MIN, RANF_NUMBER_MIDLE)
    symbols = random.choice('+-*')
    number = f'{rand_num_1} {symbols} {rand_num_2}'
    correct_answer = str(eval(f'{rand_num_1} {symbols} {rand_num_2}'))
    return number, correct_answer
