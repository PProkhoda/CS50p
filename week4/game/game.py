import random

while True:
    try:
        i = int(input("Level: "))
        if int(i) > 0:
            q = random.randrange(i)
    except ValueError:
        pass
    else:
        break
    
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < q:
                print("Too small!")
            elif guess > q:
                print("Too large!")
            else:
                print("Just right!")
                break
    except ValueError:
        pass

        