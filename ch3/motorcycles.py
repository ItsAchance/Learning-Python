# Manipulating lists

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

#motorcycles.append("harley davidson")
#print(motorcycles)

motorcycles.insert(0, "ducatti")
#print(motorcycles)

#del motorcycles[0]
#print(motorcycles)

#popped_motorcycles = motorcycles.pop(0)
#print(f"The first motorcycle I owned was a {popped_motorcycles.title()}.")

too_expensive = "ducatti"
motorcycles.remove("ducatti")
print(f"The motorcycle {too_expensive.title()} is too expensive!")
