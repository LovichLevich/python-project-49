import random


RAND_NUMBER_MIN = 1
RAND_NUMBER_MAX = 50
PROGRESSION_LENGTHT = 10
MIN_STEP_IN_PROGRESSION = 1
MAX_STEP_IN_PROGRESSION = 5

QUESTION = 'What number is missing in the progression?'


def create_numbers_in_question():
    start_number = random.randint(RAND_NUMBER_MIN, RAND_NUMBER_MAX)
    step = random.randint(MIN_STEP_IN_PROGRESSION, MAX_STEP_IN_PROGRESSION)
    number = [start_number + i * step for i in range(PROGRESSION_LENGTHT)]
    random_index = random.randint(0, len(number) - 1)
    correct_answer = str(number[random_index])
    number[random_index] = '..'
    game_question = ' '.join(map(str, number))
    return game_question, correct_answer
