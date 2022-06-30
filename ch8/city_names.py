def city_country(city, country):
	c = city
	co = country
	info = f"{c}, {co}"
	return info.title()

place0 = city_country("jönköping", "sweden")
print(place0)

place1 = city_country("islamabad", "pakistan")
print(place1)

place2 = city_country("palma de mallorca", "spain")
print(place2)
