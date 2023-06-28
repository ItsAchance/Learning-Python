favorite_number = {
	"alexander" : [13, 23],
	"johannes" : [7],
	"oscar" : [2, 5],
	"simon" : [100, 1],
	"morgan" : [666, 999]	
	}

for dude, number in favorite_number.items():
	print(f"{dude.title()}s favorite number is: ")
	for num in number:
		print(f"{num}")
