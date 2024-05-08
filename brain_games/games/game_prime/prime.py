from random import randint


RAND_NUMBER_MIN = 1
RAND_NUMBER_MAX = 100

questions = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def number_in_questions():
    number = randint(RAND_NUMBER_MIN, RAND_NUMBER_MAX)
    if answer_in_questions(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer


def answer_in_questions(number):
    if number > 1:
        for n in range(2, number):
            if (number % n) == 0:
                return False
        return True
    else:
        return False
