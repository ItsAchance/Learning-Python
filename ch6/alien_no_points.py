# Use get() to avoid an error when trying to use a key that doesnt exist.

alien_0 = {
	"color" : "green",
	"speed" : "slow"
	}
point_value = alien_0.get("points", "No point value assigned")
print(point_value)