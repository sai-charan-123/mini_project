import random

def guess_num():
	number=random.randint(1,10)
	guess=None

	while guess!=number:
		guess=int(input("guess a num between 1-10 :")) 
		if guess<number:   								#if your guess is lesser than the given numbers then print your guess is wrong
			print("your guess is wrong!,please try again")
		elif guess>number: 								#if your guess is greater than the given numbers the print your guess is too high or invalid
				print("the given number is too high!,please try again")
		else:     										#after guessing correctly the number then print your guess is correct!,thanku for playing
			print("you guess correctly, THANK YOU FOR PLAYING")
			break 										 #is used to stop the loop after guessing correctly by the user
guess_num()												 #calling the function by its name.