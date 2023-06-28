#Using every function from this chapter

cities = ["malmö", "stockholm", "göteborg", "oslo", "helsinki", "alingsås", "borås"]
print(f"Original list of cities: {cities}")

worst_city = cities.pop(-1)
print(f"Let's remove the worst city on the list: {worst_city}")

print(f"\nThe remaining cities are: {cities}")
print(f"Let's sort the cities in alphabetical order {sorted(cities)}")

print("\nUppsala is one of the major cities in Sweden, let's add it to the list")
cities.append("uppsala")
print(sorted(cities))

cities.remove("helsinki")
print(f"\nOne of the cities on the list has been removed {cities}")

cities.insert(0, "helsinki")
print(f"\nAnd now it has been added again, however now it's first in the list when unsorted")
print(cities)

cities.reverse()
print(f"\nThis is the reverse list order: {cities}")

del cities[2]
print(f"\nDuring the return to unsorted list form, another city has been removed {cities}")

cities_number = len(cities)
print(f"\nLet's see how many cities are left on the list: {cities_number}")

print(f"\nAnd the cities are: {cities}")
