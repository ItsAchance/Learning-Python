games = ["castlevania", "super mario", "tekken", "chrono trigger", "metal gear solid", "pokemon", "final fantasy", "donkey kong", "the legend of zelda"]
copy_games = games[:]

print("The first the items in the list are:")
for game in copy_games[:3]:
	print(game.title())

print("\nSome items in the middle are:")
for game in copy_games[4:7]:
	print(game.title())

print("\nThe last three items in the list are:")
for game in copy_games[-3:]:
	print(game.title())
