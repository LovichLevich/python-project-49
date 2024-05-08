import prompt


LIMIT_ROUND = 3
STEP_COUNT = 1
START_COUNTER = 0


def game_logic(data):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    print(data.questions)
    correct_count = START_COUNTER
    for _ in range(LIMIT_ROUND):
        number, correct_answer = data.number_in_questions()
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if  correct_answer == user_answer:
            print("Correct!")
        else:
            print(f"{user_answer} is the wrong answer;(."
                  f"The correct answer was {correct_answer}.")
            print(f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")
