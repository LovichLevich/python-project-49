import prompt


ROUNDS_COUNT = 3


def game_generate(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.QUESTION)
    for _ in range(ROUNDS_COUNT):
        game_question, correct_answer = game.create_numbers_in_question()
        print(f'Question: {game_question}')
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            print('Correct!')
        else:
            print(f'{user_answer} is the wrong answer;(.'
                  f'The correct answer was {correct_answer}.')
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
