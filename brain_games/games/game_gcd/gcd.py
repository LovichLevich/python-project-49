import math
import random


RAND_NUMBER_MIN = 1
RAND_NUMBER_MAX = 100

questions = 'Find the greatest common divisor of given numbers.'


def number_in_questions():
    rand_num_1 = random.randint(RAND_NUMBER_MIN, RAND_NUMBER_MAX)
    rand_num_2 = random.randint(RAND_NUMBER_MIN, RAND_NUMBER_MAX)
    number = f'{rand_num_1} {rand_num_2}'
    correct_answer = str(math.gcd(rand_num_1, rand_num_2))
    return number, correct_answer
