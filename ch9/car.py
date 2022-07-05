class Car():
	"""A simple attempt to represent a car"""

	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car"""
		self.make = make
		self.model = model
		self.year = year

	def get_desctiptive(self):
		"""Return a neatly formtatted descriptive name"""
		long_name = f"{str(self.year)} {self.make} {self.model}"
		return long_name.title()

my_new_car = Car("Tesla", "Model S", "2022")
print(my_new_car.get_desctiptive())
