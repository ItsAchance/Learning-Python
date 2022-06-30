def build_profile(first, last, **user_info):
	"""Build a dictonary containing everything we know about a user."""
	profile = {}
	profile["first_name"] = first
	profile["last_name"] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

profile = build_profile("alexander", "chance", role = "network engineer", hometown = "jönköping")
print(profile)