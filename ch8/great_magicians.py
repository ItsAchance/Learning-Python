magicians = ["joe labero", "tobbe trollkarl", "gandalf", "radagast"]

def show_magicians(magicians):
	print(magicians)

great_magicians = []

def make_great(great_magicians):
	"""Adding 'The Great' to each magician"""
	while magicians:
		making_magicians = magicians.pop()
		great_magicians.append(making_magicians)
	
	for magician in great_magicians:
		print(f"The Great {magician.title()}!")


make_great(great_magicians)
show_magicians(magicians)