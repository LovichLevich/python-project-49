from random import randint

RAND_NUMBER_MIN = 1
RAND_NUMBER_MAX = 100

questions = 'Answer "yes" if the number is even, otherwise answer "no".'
def number_in_questions():
    number = randint(RAND_NUMBER_MIN, RAND_NUMBER_MAX)
    if answer_in_questions(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer

def answer_in_questions(number):
    return number % 2 == 0
