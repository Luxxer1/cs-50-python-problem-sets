from random import randrange

n = 0

while n < 1:
    try:
        n = int(input("Level: "))
    except ValueError:
        pass

randomNumber = randrange(1, int(n) + 1)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            pass
        if guess == randomNumber:
            print("Just right!")
            break
        elif guess > randomNumber:
            print("Too large!")
        else:
            print("Too small!")
    except ValueError:
        pass
