rivers = {
	"nile" : "egypt",
	"sepik river" : "new guinea",
	"volga river" : "moscow"
	}

# This prints the river and the city
#for river, city in rivers.items():
#	print(f"The {river.title()} runs through {city.title()}.")

# This print only the key (the name of the river)
#for river in rivers.keys():
#	print(river.title())

# This prints the value (city name the river runs through)
for city in rivers.values():
	print(city.title())
