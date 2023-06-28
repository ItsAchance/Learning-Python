#Creating an empty list and then appending all number from 1 to 1000000 in it

numbers = []
for number in range(1, 1000001):
	numbers.append(number)
	
#print(numbers)


#print(min(numbers))
#print(max(numbers))
print(sum(numbers))