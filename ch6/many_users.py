users = {
	"aesinstein" : {
		"first" : "albert",
		"last" : "einstein",
		"location" : "princeton"
	},
	"mcurie" : {
		"first" : "marie",
		"last" : "currie",
		"location" : "paris"
	},
}

for user_name, user_info in users.items():
	print(f"\nUsername: {user_name}")

	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']
	print(f"\tFullname: {full_name.title()}")
	print(f"\tLocation: {location.title()}")
