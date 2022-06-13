sandwich_orders = ["ham sandwich", "egg sandwich", "pastrami sandwich"]
finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	finished_sandwiches.append(sandwich)
for sandwich in finished_sandwiches:
	print(f"I made your {sandwich}!\n")
