"""Start with users that need to be verified and an empty list to hold confirmed users"""

unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

"""Verify each user until there are no more unconfirmed users. Move each verified user into the list of confirmed users."""

while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print(f"\nVerifying user: {current_user.title()}\n")
	confirmed_users.append(current_user)
print(f"The following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(f"{confirmed_user.title()}")