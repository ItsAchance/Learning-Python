programmers = ["martin", "alexander", "jen", "edward", "kalle"]

favorite_language = {
	"jen" : "python",
	"sarah" : "c",
	"edward" : "ruby",
	"phil" : "python"
	}

# Every coder who has already taken the poll is in the dictonary favorite_language and all the programmers are in the list programmers
for coder in programmers:
	if coder in favorite_language.keys():
		print(f"{coder.title()}, thank you for taking the poll.")
	else:
		print(f"{coder.title()}, please take our poll.")
