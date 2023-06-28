pet_0 = {
	"kind" : "dog",
	"owner" : "kevin"
	}
pet_1 = {
	"kind" : "cat",
	"owner" : "angela"
	}
pet_2 = {
	"kind" : "bear",
	"owner" : "dwight"
	}
pet_3 = {
	"kind" : "snake",
	"owner" : "creed"
	}

pets = [pet_0, pet_1, pet_2, pet_3]

for pet in pets:
	print(f"{pet['owner'].title()} has a {pet['kind']}")