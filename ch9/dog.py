class Dog():
	"""A simple attempt to model a dog."""

	def __init__(self, name, age):
		"""Initialize name and age attributes"""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in respone to a command"""
		print(f"{self.name.title()} is now sitting")

	def roll_over(self):
		"""Simulate rolling over in response to a command"""
		print(f"{self.name.title()} rolled over!")
	def bark(self):
		"""Simulate barking at command"""
		print(f"{self.name.title()} barked!")


my_dog = Dog("wille", 14)
your_dog = Dog("zigge", 14)

print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old")

print()
my_dog.sit()
my_dog.roll_over()

print()
print(f"Your dog's name is {your_dog.name.title()}.")
print(f"Your dog is {your_dog.age} years old!")
your_dog.sit()
print()
my_dog.bark()
