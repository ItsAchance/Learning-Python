prompt = """Please enter your desired toppings for the pizza, please enter 'quit' when you are done: """

while True:
	toppings = input(prompt)
	if toppings == "quit":
		break
	else:
		print(f"{toppings} added to your toppings")