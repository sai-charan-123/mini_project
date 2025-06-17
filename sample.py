import random

def guess_num():
    number = random.randint(1, 10)

    while True: #the keyword true is used to repeate the loop and this will stop when break statement is given.
        try: #we used the exception handling block to understand the code clearly.
            guess = int(input("Guess the number between 1 to 10: "))#asking the user to give input.
            if guess < number: #if your guess is lesser than the given numbers then print the given num is too low
                print("The given number is Too low! Try again.")
            elif guess > number: #if your guess is greater than the given numbers the print your guess is too high 
                print("The given number is Too high! Try again.")
            else:   #after guessing correctly the number then print congratulations! you guessed correctly
                print("Congratulations! You have guessed the number correctly.")
                break # here break is used to stop the repeated loop and after guessing correctly the loop will be end.
        except ValueError: # it is used to know the wrong stetement passed by user is invalid or error based on our requirments given. 
            print("Invalid input. Please enter again.")

guess_num() #calling the function.
