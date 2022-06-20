def describe_pet(animal_type, pet_name):
	"""Display information about the pet"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet("hamster", "john")
describe_pet("cat", "salanen")



# Using default values
def describe_pet(pet_name, animal_type="dog"):
	"""Display information about the pet"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet("john")

# Using keyword arguments
describe_pet(animal_type="cat", pet_name="salanen")