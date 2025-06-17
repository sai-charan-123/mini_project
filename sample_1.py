import random

def guess_num():
    number = random.randint(1, 10)
    guess_list = []

    while True:
        try:
            a = int(input("Guess a number between 1-10: "))
        except ValueError:
            print("Please guess your number.")
            continue

        guess_list.append(a)

        if a < number:
            print("Your guess is too low! Please try again.")
        elif a > number:
            print("Your guess is too high! Please try again.")
        else:
            print("You guessed correctly! THANK YOU FOR PLAYING.")
            break

    print("You took {} attempts.".format(len(guess_list)))

guess_num()

