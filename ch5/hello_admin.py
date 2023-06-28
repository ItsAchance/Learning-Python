current_users = ["chance", "ynb924", "alexander", "olof", "rolf"]
new_users = ["olof", "rolf", "kalle", "hampus", "Chance"]


for new_user in new_users:
	if new_user.lower() in current_users:
		print(f"The username {new_user} is already taken, please pick another one")
	else:
		print(f"The username {new_user} is available")
