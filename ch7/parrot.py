prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program\t: "

active = True
while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	elif message == 'Hello there':
		print("General Kenobi!")
	else:
		print(message)