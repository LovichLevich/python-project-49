import random


RAND_NUMBER_MIN = 1
RAND_NUMBER_MAX = 50

questions = 'What number is missing in the progression?'


def generate_random_number():
    return random.randint(RAND_NUMBER_MIN, RAND_NUMBER_MAX)


def number_in_questions():
    start_number = random.randint(RAND_NUMBER_MIN, RAND_NUMBER_MAX)
    step = random.randint(1, 5)
    number = [start_number + i * step for i in range(10)]
    random_index = random.randint(0, len(number) - 1)
    correct_answer = str(number[random_index])
    number[random_index] = ".."
    return number, correct_answer
