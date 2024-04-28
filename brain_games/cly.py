def welcome_user():
  name = input('May I have your name? ')
  return f'Hello, {name}!'

greeting = welcome_user()
print(greeting)