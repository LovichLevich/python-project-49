from random import randint

RAND_NUMBER_MIN = 1
RAND_NUMBER_MAX = 100

questions = 'Answer "yes" if the number is even, otherwise answer "no".'
def number_in_questions():
    number = randint(RAND_NUMBER_MIN, RAND_NUMBER_MAX)
    return number

def answer_in_questions(generate_number):
    if generate_number % 2 == 0:
        return 'yes'
    else:
        return 'no'
random_number = number_in_questions()
correct_answer = answer_in_questions(random_number)