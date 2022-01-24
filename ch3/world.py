places = ["malmö", "stockholm", "göteborg", "köpenhamn", "oslo"]
print(places)

print(sorted(places))

print(f"Original order: {places}")

places.reverse()
print(places)
places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)