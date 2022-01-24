# Playing around with lists

guests = ["sandra", "silfver", "fraser", "thor"]
greeting0 = "Hello, and welcome to the party:"
greeting1= "You are most welcome to join the party:"

print(f"\n{greeting0} {guests[0].title()}")
print(f"\n{greeting0} {guests[1].title()}")
print(f"\n{greeting0} {guests[2].title()}")
print(f"\n{greeting0} {guests[3].title()}")

cant_come = guests.pop(3).title()

print(f"\nSadly it seems like {cant_come} cannot make it to the party.")

guests.insert(3, "ghost")

print(f"\n{greeting0} {guests[0].title()}")
print(f"\n{greeting0} {guests[1].title()}")
print(f"\n{greeting0} {guests[2].title()}")
print(f"\n{greeting0} {guests[3].title()}")

print(f"\n\nIt would seem like we have acquired a bigger table, we will have to invite more people to our party!!")

guests.insert(0, "zigge")
guests.insert(2, "tillan")
guests.append("tomten")

print(f"\n{greeting0} {guests[0].title()}")
print(f"\n{greeting0} {guests[1].title()}")
print(f"\n{greeting0} {guests[2].title()}")
print(f"\n{greeting0} {guests[3].title()}")
print(f"\n{greeting0} {guests[4].title()}")
print(f"\n{greeting0} {guests[5].title()}")
print(f"\n{greeting0} {guests[6].title()}")

print(f"\n\nUnfortunaletly there has been an error and it seems like we only have two spots for the party")

uninvited0 = guests.pop(0).title()
uninvited1 = guests.pop(2).title()
uninvited2 = guests.pop(2).title()
uninvited3 = guests.pop(2).title()
uninvited4 = guests.pop(2).title()

print(f"\nI'm sorry {uninvited0} there is no room for you")
print(f"\nI'm sorry {uninvited1} there is no room for you")
print(f"\nI'm sorry {uninvited2} there is no room for you")
print(f"\nI'm sorry {uninvited3} there is no room for you")
print(f"\nI'm sorry {uninvited4} there is no room for you")

print(f"\nI have great news for you {guests[0].title()} you are still invited to the party!")
print(f"\nI have great news for you {guests[1].title()} you are still invited to the party!")

del guests[0]
del guests[0]
print(guests)

print(len(guests))
