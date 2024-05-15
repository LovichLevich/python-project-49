import random

RAND_NUMBER_MIN = 1
RAND_NUMBER_MIDDLE = 50
RAND_NUMBER_MAX = 100

QUESTION = 'What is the result of the expression?'


def create_numbers_in_question():
    rand_num_1 = random.randint(RAND_NUMBER_MIDDLE, RAND_NUMBER_MAX)
    rand_num_2 = random.randint(RAND_NUMBER_MIN, RAND_NUMBER_MIDDLE)
    operator = random.choice('+-*')
    game_question = f'{rand_num_1} {operator} {rand_num_2}' #The variable is named "number" 
    #because of its further implementation in the def game_generate(game) function. 
    correct_answer = str(evaluate(rand_num_1, operator, rand_num_2))
    return game_question, correct_answer


def evaluate(num_1, symbol, num_2):
    if symbol == '+':
        return num_1 + num_2
    elif symbol == '-':
        return num_1 - num_2
    else:
        return num_1 * num_2
