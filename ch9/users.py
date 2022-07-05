class User():
	"""A class of a user"""

	def __init__(self, first_name, last_name, age, user_name):
		"""Initialze several attributes"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.user_name = user_name

	def describe_user(self):
		"""A method describing a user and printing the output"""
		print(f"The user {self.user_name}'s real name is {self.first_name.title()} {self.last_name.title()} and is {self.age} old")

	def greet_user(self):
		"""A method greeting a user"""
		print(f"Hello {self.first_name.title()} {self.last_name.title()}")

mr_chance = User("alexander", "chance", 29, "achance")
mr_silfver = User("mattias", "silfver", 33, "madtoes")
mr_chance.describe_user()
mr_silfver.describe_user()
print()

mr_chance.greet_user()
mr_silfver.greet_user()
