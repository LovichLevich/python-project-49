import random


print('What is the result of the expression?')

def generate_random_sum():
    rand_num_1 = random.randint(50, 100)
    rand_num_2 = random.randint(1, 50)
    symbols = ["+", "-", "*"]
    random_symbol = random.choice(symbols)
    print(f"Question: {rand_num_1} {random_symbol} {rand_num_2}")
    
def correct_answer(rand_num_1, rand_num_2):
    if random_symbol == "+":
        return rand_num_1 + rand_num_2
    elif random_symbol == "-":
        return rand_num_1 - rand_num_2
    else:
        return rand_num_1 * rand_num_2
    



