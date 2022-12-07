# create function Guessnumber
def Guessnumber():
    import random

    tries = 0
    number = random.randint(1, 100)
    guess = int(input("Guess a number between 1 and 100: "))
    while guess != number:
        if guess < number:
            print("Too low")
            guess = int(input("Guess again: "))
        elif guess > number:
            print("Too high")
            guess = int(input("Guess again: "))
        1
        tries += 1
    if guess == number:
        print("You guessed it!"+ " It took you " + str(tries+1) + " tries.")
        print("The number was " + str(number))

Guessnumber()