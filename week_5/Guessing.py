from random import randrange


def Guessing():
    random_number = randrange(1, 100)
    print("Guess a number between 1 and 100")
    print("You have 5 attempts")
    guess = int(input("Your guess: "))
    count = 1
    while guess != random_number:
        if count > 4:
            print("You are out of guesses")
            print("The number was %d" % random_number)
            break
        if guess < random_number:
            print("Too low, you have %d guesses left" % (5 - count))
            count += 1
            guess = int(input("Another guess: "))
        else:
            print("Too high,  you have %d guesses left" % (5 - count))
            count += 1
            guess = int(input("Another guess: "))
    else:
        print("Congratulations, you guessed the number")
        print("Random number was: %d" % random_number)


Guessing()
