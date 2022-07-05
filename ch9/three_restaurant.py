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

restaurant_brödernas = Restaurant("brödernas", "burgers")
restaurant_v = Restaurant("v", "pizza")
restaurant_thap_thim = Restaurant("thap thim", "thai")

restaurant_brödernas.describe_restaurant()
print()
restaurant_v.describe_restaurant()
print()
restaurant_thap_thim.describe_restaurant()
print()