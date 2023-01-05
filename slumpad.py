import random

difficulty = input("Before we start the game we need to configure the setting\nPlease enter your diffuculty level:\nEasy\nMedium\nHard\n: ")
if difficulty.lower() == "easy":
	tries = 10 
elif difficulty.lower() == "medium":
	tries = 7
elif difficulty.lower() == "hard":
	tries = 5
else:
	print("That is not an option\nClosing the game...")
	quit()
top_range_number = int(input(f"You have chosen {difficulty} and now you need to pick a number: "))

number = random.randint(1,top_range_number)
guess = 0

print(f"\nHello and welcome to SLUMPAD. Try to guess the number the computer is thinking of.\nYou have {tries} tries, Good luck!\n\n")
while guess != number:
	guess = int(input(f"Guess a number betwwen 1 and {top_range_number}: "))
	if tries == 1:
		print(f"Sorry you are out of tries. The correct number is {number}")
		break
	elif guess < number:
		tries -= 1
		print(f"The number is higher than {guess}\nYou have {tries} tries left.\n")
	elif guess > number:
		tries -= 1
		print(f"The number is lower than {guess}\nYou have {tries} tries left\n")
	elif guess == number:
		print(f"\nCongratulations, the correct number is {number}!")