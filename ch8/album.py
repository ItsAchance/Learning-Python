def make_album(artist, album):
	album_dict = {
		"artist" : artist,
		"album" : album
		}
	return album_dict

first_album = make_album("in flames", "colony")
print(first_album)

second_album = make_album("ghost", "meloria")
print(second_album)

third_album = make_album("slipknot", "iowa")
print(third_album)


def complete_album(artist, album, tracks=None):
	album_info_dict = {
		"artist" : artist,
		"album" : album
		}
	if tracks:
		album_info_dict["tracks"] = tracks
	return album_info_dict

new_first_album = complete_album("metallica", "master of puppets" ,tracks=8)
print(new_first_album)

new_second_album = complete_album("children of bodom", "are you dead yet")
print(new_second_album)