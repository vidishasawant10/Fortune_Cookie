import random

print(random.randint(1,10))
print(random.random()) #print values between 0 and 1

def random_ball():
    ball = ["Yes", "No", "Maybe"]
    return random.choice(ball)

question = input("Is this the right answer? ")
answer = print(random_ball())

def random_ballgame():
    answer = random.randint(1,3)

    if answer == 1:
        print(answer,"Yes")
    elif answer == 2:
        print(answer,"No")
    elif answer == 3:
        print(answer,"Maybe")

random_ballgame()
