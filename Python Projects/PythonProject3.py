# ------------------------------ GUESSING GAME --------------------------------
import random 
number = random.randint(40,50)

player_name = input('Hello,Whats your name ')
number_of_guesses = 0
print('okay '+ player_name + '.........Guess a number between 40 and 50')

while number_of_guesses < 45:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in'+str(number)+'tries!!')
else:
    print('You did not guess the number,My number was'+str(number))
