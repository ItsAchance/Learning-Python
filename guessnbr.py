import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Gissa på ett nummer mellan 1 och {x}: "))
        if guess < random_number:
            print("Fel gissat, gissa på en högre siffra")
        elif guess > random_number:
            print("Fel gissat, gissa på en lägre siffra")

    print(f"Du gissade på {random_number} och det var rätt!!")


guess(20)
