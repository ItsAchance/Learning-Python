def make_car(manufacturer, model, **misc):
	car = {}
	car["maker"] = manufacturer
	car["model"] = model
	for key, value in misc.items():
		car[key] = value
	return car

my_car = make_car("Tesla", "Model S", color = "Black", auto_pilot = "False", machine_guns = "False", fly_mode = "True")
print(my_car)