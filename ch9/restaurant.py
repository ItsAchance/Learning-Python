class Restaurant():
	"""A model of a restaurant"""

	def __init__(self, name, cuisine_type):
		"""Initialize name and cuisine_type attributes"""
		self.name = name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"This restaurant is called {self.name.title()}. It is serving the following type of cuisine: {self.cuisine_type.title()}.")

	def open_restaurant(self):
		print(f"The restaurant is open for business!")

restaurant = Restaurant("spot", "italian")


restaurant.describe_restaurant()
restaurant.open_restaurant()