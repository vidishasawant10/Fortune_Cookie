import random

print(random.randint(1, 10))
print(random.random())  # print values between 0 and 1


def fortune_cookie():
    ball = ["You will have a good day", "You will have a dull day", "Your day can be good or bad"]
    return random.choice(ball)


question = input("How will be my day today? ")
answer = print(fortune_cookie())


def lucky_number():
    luckynumber = random.randint(1, 100)
    print(f"Your lucky number for today is {luckynumber}")


lucky_number()


def random_ballgame():
    answer = random.randint(1, 3)

    if answer == 1:
        print(answer, "Yes")
    elif answer == 2:
        print(answer, "No")
    elif answer == 3:
        print(answer, "Maybe")


random_ballgame()
