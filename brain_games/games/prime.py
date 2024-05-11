from random import randint


RAND_NUMBER_MIN = 1
RAND_NUMBER_MAX = 100

QUESTIONS = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def create_numbers_in_question():
    number = randint(RAND_NUMBER_MIN, RAND_NUMBER_MAX)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer


def is_prime(number):
    if number <= 1:
        return False
    for n in range(2, number):
        if (number % n) == 0:
            return False
    return True
