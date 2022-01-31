games = ["castlevania", "super mario", "tekken", "chrono trigger", "metal gear solid", "pokemon", "final fantasy", "donkey kong", "the legend of zelda"]
members = ["snake", "mario", "cloud", "jin", "chrono", "link", "alucard,"]
rent_cost = 50
jolt_cola = True
burgare = False

if "castlevania" in games:
	print("We have castlevania!")
else:
	print("We do not have castlevania")

if (len(games)) == (8):
	print("\nThere are nine games available")
else:
	print("\nWe do not have nine games available")

if rent_cost == 100:
	print("\nI would like to rent a game")
elif rent_cost >= 50:
	print("\nI would like to rent two games!")
else:
	print("\nWow, that was expensive, sorry I am not renting a game today")

if jolt_cola == True:
	print("\nI would like to order a jolt cola as well, thank you")
else:
	print("\nI have everything I need for now thank you")

member = "clOud"
if member.lower() in members:
	print(f"\nWelcome {member.title()}")
else:
	print("\nWould you like to become a member?")

if burgare != True:
	print("\nWe have burgers")
else:
	print("\nSorry, we do not have burgers")

if jolt_cola and burgare == True:
	print("\nWould you like to try our menu?")
else:
	print("\nWould you like just Jolt or Burgare?")

if jolt_cola or burgare == True:
	print("\nSorry we cannot offer a menu")
else:
	print("\nWould you like to try our menu?")
