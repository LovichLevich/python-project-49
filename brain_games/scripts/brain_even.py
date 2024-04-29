import random


print('Welcome to the Brain Games!')
user_name = input("May I have your name?: ")
print(f"Hello, {user_name}!")
print('Answer "yes" if the number is even, otherwise answer "no".')
correct_count = 0
while correct_count < 3:
    rand_num = random.randint(1, 100)
    print(f"Question: {rand_num}")
    answer_user = input("Your answer: ").lower()
    if rand_num % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    if correct_answer == answer_user:
        correct_count += 1
        print("Correct!")
    else:
        correct_count = 0
        print(f"{answer_user} is the wrong answer ;(", end="")
        print(f"The correct answer was {correct_answer}.")
        print(f"Let's try again, {user_name}!")

print(f"Congratulations, {user_name}!")
