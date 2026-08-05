secret = 7

while True:
    guess = int(input("Guess a number (1-10): "))

    if guess < secret:
        print("Your guess is too low!")
    elif guess > secret:
        print("Your guess is too high!")
    else:
        print("Your guess is correct!!")
        break