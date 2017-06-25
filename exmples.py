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
guess = None
while random_number != guess:
    guess = input()
    print('Sorry, not the number I was thinking of, try again.... Guess count is', guess_count)
    guess_count += 1
    continue

print('Hey, you got it, you said', random_number, 'and that\'s what I was thinking of!')
sys.exit()