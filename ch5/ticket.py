age = input("How old are you? ")
age = int(age)

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 60:
	price = 45
else:
	price = 20

print(f"Your ticket price is {price}")
