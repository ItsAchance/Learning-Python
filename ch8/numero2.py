def create_profile(first, last, **other_info):
	profile = {}
	profile["first_name"] = first
	profile["last_name"] = last
	for key, value in other_info.items():
		profile[key] = value
	return profile

person0 = create_profile("mattias", "silfver", role = "guest", title = "king")
print(person0)

person1 = create_profile("Mr", "X", type = "unknown")
print(person1)

person2 = create_profile("Solid", "Snake", favorite_line = "Kept you waiting huh?")
print(person2)