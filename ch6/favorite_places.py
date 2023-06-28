favorite_places = {
	"ben" : ["stockholm, oslo"],
	"beth" : ["london, glasgow, dublin"],
	"jack" : ["toronto, ottawa"]
}

for person, city in favorite_places.items():
	print(f"{person.title()}s favorite places are: ")
	for town in city:
		print(f"{town.title()}\n")