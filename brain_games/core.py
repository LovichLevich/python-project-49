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
    number_in_question = {data.random_number}
    while correct_count < LIMIT_ROUND:
        print(f"Question: {number_in_question}")
        user_answer = prompt.string('Your answer: ')
        if data.correct_answer == user_answer:
            correct_count += STEP_COUNT
            print("Correct!")
        else:
            print(f"{user_answer} is the wrong answer")
            print(f"The correct answer was {data.correct_answer}.")
            print(f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")
