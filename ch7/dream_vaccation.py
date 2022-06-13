dream_vaccation = {}
polling_status_active = True

while polling_status_active:
	name = input("Whats is your name? ")
	destination = input("Where is your dream vaccation? ")

	dream_vaccation[name] = destination

	repeat = input("\nWould anyone else like to add their dream vaccation? (yes/no) ")
	if repeat == "no":
		polling_status_active = False
for name, destination in dream_vaccation.items():
	print(f"\n{name.title()}s dream vaccation is {destination.title()}")