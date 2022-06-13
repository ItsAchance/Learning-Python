sandwich_orders = ["pastrami sandwich", "ham sandwich", "egg sandwich", "pastrami sandwich", "veggie sandwich", "pastrami sandwich", "mozarella sandwich"]
finished_sandwiches = []

print("Unfortunately we do not have any pastrami sandwiches left.")

"""Remove all the pastrami sandwiches"""

while "pastrami sandwich" in sandwich_orders:
	sandwich_orders.remove("pastrami sandwich")
	sandwich = sandwich_orders.pop()

""" Print out the rest of the sandwiches"""

for sandwich in sandwich_orders:
	finished_sandwiches.append(sandwich)
	print(f"\nWe made your {sandwich}")
