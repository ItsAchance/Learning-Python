def make_album(artist, album):
	album_info_dict = {
		"artist" : artist,
		"album" : album
		}
	return album_info_dict

while True:
	print("Which artist to you want to enter?: ")
	print("enter 'q' to quit at any time")
	some_artist = input("Artist: ")
	if some_artist == "q":
		break
	
	print("Which album do you wanna enter?: ")
	print("enter 'q' at any time to quit")
	some_album = input("Album: ")
	if some_album == "q":
		break
	
	complete_album = make_album(some_artist, some_album)
	print(complete_album)
