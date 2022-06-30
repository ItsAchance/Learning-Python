"""importing the 'make_pizza' funtion from the module pizza"""
#from pizza import make_pizza

"""importing the 'make_pizza' funtion from the module pizza and making an alias for the funtion"""
#from pizza import make_pizza as mp

"""importing the module pizza and giving it the alias 'p' """
import pizza as p

p.make_pizza("medium", "pepperoni")
p.make_pizza("large", "kebab", "ham", "kebabsauce", "cheese", "fries")