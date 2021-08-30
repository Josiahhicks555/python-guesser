#got it working mostly but after the computer makes a guess it stopes guessing idk why and inorder to make a new guess it makes you kill the terminal

import random as r

guess_number = 0


while guess_number < 1 or guess_number > 100:
    guess_number = int(input("guess a number between 1 and 100: "))

if(guess_number > 100):
    print("The number is <= 100")
if guess_number < 1:
    print("The number is >= 1")

computer_guess = r.randint(1, 100)

print("computer guesses.", computer_guess)



while computer_guess != guess_number:
    if computer_guess > guess_number:
        computer_guess -= 1
        computer_guess = r.randint(1, computer_guess)

else:
    computer_guess += 1
    computer_guess = r.randint(computer_guess, 100)
    print ("the computer guesses.", computer_guess)
print ("the computer guesses", computer_guess, "witch was the correct guess!")
