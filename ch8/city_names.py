def city_country(city, country):
	c = city
	co = country
	info = f"{c}, {co}"
	return info.title()

place0 = city_country("jönköping", "sweden")
print(place0)