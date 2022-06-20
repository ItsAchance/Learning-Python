programmers = ["martin", "alexander", "jen", "edward", "kalle"]

favorite_language = {
	"jen" : ["python", "ruby"],
	"sarah" : ["c"], 
	"edward" : ["ruby", "go"],
	"phil" : ["python", "haskell"],
	}

# Every coder who has already taken the poll is in the dictonary favorite_language and all the programmers are in the list programmers
for coder in programmers:
	if coder in favorite_language.keys():
		print(f"{coder.title()}, thank you for taking the poll.")
	else:
		print(f"{coder.title()}, please take our poll.")

#This prints out the coder and their favorite language
for coder, languages in favorite_language.items():
	print(f"\n{coder.title()}'s favorite language is: ")
	for language in languages:
		print("\t" + language.title())
