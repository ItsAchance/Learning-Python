favorite_number = {
	"alexander" : 13,
	"johannes" : 7,
	"oscar" : 2,
	"simon" : 100,
	"morgan" : 666	
	}

print(f"Alexander's favorite number is {favorite_number['alexander']}")
print(f"Johannes's favorite number is {favorite_number['johannes']}")
print(f"Oscar's favorite number is {favorite_number['oscar']}")
print(f"Simon's favorite number is {favorite_number['simon']}")
print(f"Morgan's favorite number is {favorite_number['morgan']}")

# The same thing but looping through the dictonary

for k, v in favorite_number.items():
	print(f"\n{k.title()}'s favorite number is {v}")