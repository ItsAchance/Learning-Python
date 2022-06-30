def make_sandwich(*toppings):
	print("\nMaking a sandwich with the following toppings: ")
	for topping in toppings:
		print(f"- {topping}")

make_sandwich("ham", "burrata")
make_sandwich("cheese", "marmelade")
make_sandwich("avocado", "eggs", "herb salt")