while True:
	age = input("Please enter your age: ")
	age = int(age)
	if age < 3:
		print("Your ticket is free of charge")
		break
	elif age < 12:
		print("That will be 10$ please")
		break
	else:
		print("That will be 15$ please")
		break
