import sys
import random

print('Hello, what\'s your name?')
person_name = input()
print('Hey', person_name, 'how is it going?')
print('Now... what\'s your age?')
person_age = input()
print ('OK', person_name,'So you\'re', person_age, 'years old. Got it')
random_number = random.randrange(0,20)
print('I\'m thinking of a number between 0 and 20, go ahead and guess it!')
print('Debug: ', random_number)
guess_count = 1

print('OK, guess a number')
while random_number != int(guess):
    guess = input()
    guess_count += 1
    print(guess,'is not the number I\'m thinking of, try again')

print('Yep', random_number, 'was it and it took you', guess_count, 'tries!')

sys.exit()