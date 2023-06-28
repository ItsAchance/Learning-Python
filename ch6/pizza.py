pizza = {
	"crust" : "thick",
	"toppings" : ["mushrooms", "extra cheese"]
	}

# Summarize the order
print(f"You ordered a pizza with {pizza['crust']} crust with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping.title())