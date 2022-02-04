aliens = []

# Make 30 green aliens
for alien_number in range(30):
	new_alien = {"color" :"green", "points" : 5, "speed" : "slow"}
	aliens.append(new_alien)

# Show the first 5 aliens
#for alien in aliens[:5]:
#alien_0 = {"color" : "green", "points" : 5}	print(alien)

# Show all the created aliens
#for alien in aliens:
#	print(alien)

# Show how many aliens have been created
#print(len(aliens))

# Change characteristics of the first three aliens
for alien in aliens[:3]:
	if alien['color'] == "green":
		alien['color'] = "yellow"
		alien['speed'] = "medium"
		alien['points'] = 10
	elif alien['color'] == "yellow": # If we have yellow aliens in the list
		alien['color'] = "red"
		alien['speed'] = "fast"
		alien['points'] = 15

# Print the first 5 aliens in the list aliens
for alien in aliens[:5]:
	print(alien)