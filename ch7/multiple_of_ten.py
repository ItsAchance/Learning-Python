number = input("Please enter a number and I'll tell you if it's a multiple of ten or not: ")
number = int(number)

if number % 10 == 0:
	print(f"\nYour number is a multiple of ten!")
else:
	print(f"\nYour number is not a multiple of ten!")