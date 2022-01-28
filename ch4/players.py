players = ["alexander", "willy", "simon", "morgan", "christoffer", "hamdija", 
"johannes", "oscar"]
mkb_dudes = players[:]
svikare = players[:]
balkan = players[:]

print("These are the OG's:")
for player in players[:2]:
	print(player.title())

print("\nHere are all the current dudes:")
for dude in mkb_dudes[:4]:
	print(dude.title())

print("\nDessa är svikare:")
for svek in svikare[-2:]:
	print(svek.title())

print("\nHär har vi burek boys:")
for burek in balkan[4:6]:
	print(burek.title())
