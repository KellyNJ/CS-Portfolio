import random

while True:
    maxValue = int(input("Enter a maximum value: "))
    number = random.randint(0, maxValue)
    guess = None
    count = 1
    while guess != number:
        guess = int(input("Guess the number: "))
        if guess < number:
            if number-guess < 4:
                print("Try again, guess is close but still too low.")
            else:
                print("Try again, guess is too low.")
            count += 1
        elif guess > number:
            if guess-number < 4:
                print("Try again, guess is close but still too high.")
            else:
                print("Try again, guess is too high.")
            count += 1
        else:
            print("You guessed the number in",count,"guesses!")
            cont = input("Do you want to play again (Y/N)? ")
            if cont == 'N':
                exit()
