pizzas = ["kebabpizza", "hawaiipizza", "calzone"]
friend_pizzas = pizzas[:]

pizzas.append("vesuvio")
friend_pizzas.append("africana")

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza.title())

print("\nMy friends favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza.title())

