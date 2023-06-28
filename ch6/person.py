person_0 = {
	"first_name" : "john",
	"last_name" : "doe",
	"age" : 29,
	"city" : "malmö"
	}
person_1 = {
	"first_name" : "kalle",
	"last_name" : "kula",
	"age" : 34,
	"city" : "göteborg"
	}
person_2 = {
	"first_name" : "anders",
	"last_name" : "andersson",
	"age" : 42,
	"city" : "stockholm"
	}

people = [person_0, person_1, person_2]

for person in people:
	print(f"\nFirstname: {person['first_name'].title()}")
	print(f"Lastname: {person['last_name'].title()}")
	print(f"Age: {person['age']}")
	print(f"City: {person['city'].title()}")