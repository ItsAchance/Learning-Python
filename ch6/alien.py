# Track the movement of alien_0 depending on its speed.

alien_0 = {
<<<<<<< HEAD
	"x_position" : 0,
	"y_position" : 25, 
	"speed" : "medium", 
	"color" : "green", 
	"points" : 5
	}

=======
		"x_position" : 0,
		"y_position" : 25,
		"speed" : "medium",
		"color" : "green",
		"points" : 5
		}
		
>>>>>>> origin/main
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed

if alien_0["speed"] == "slow":
	x_increment = 1
elif alien_0["speed"] == "medium":
	x_increment = 2
else:
	# This must be a fast alien
	x_increment = 3
# The new position is the old position plus the increment

alien_0["x_position"] = alien_0["x_position"] + x_increment
#print(f"The new position is: {alien_0['x_position']}")

# Deleting a key and priting the dictonary to verify its deleted
print(f"The alien {alien_0['color']} is worth {alien_0['points']}")

del alien_0["points"]
print(alien_0)
