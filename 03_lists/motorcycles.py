motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# changing an item in the list
motorcycles[0] = 'ducati'
print(motorcycles)

# adding new item to the list 
motorcycles.append('ducati')
print(motorcycles)

# create empty list 
new_motorcycles = []
new_motorcycles.append('honda')
new_motorcycles.append('suzuki')
new_motorcycles.append('kawasaki')

print(new_motorcycles)

#inserting new value into the first position of the list

motorcycles.insert(0, 'kawasaki')
print(motorcycles)

#removing an item using the del Statement 
del motorcycles[0]
print(motorcycles)

del motorcycles[2]
print(motorcycles)

# using pop function - removes last item in the last and saves it in the variable so it can be used again
motorcycles = ['honda', 'yamaha', 'suzuki']
print(f"\n{motorcycles}")

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#example of pop usage
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"\nThe last motorcycle I owned was a {last_owned.title()}")

#removing any position from the list by adding index into () - parentheses
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"\nThe first motorcycle I owned was a {first_owned.title()}.\n ")

# remove method - removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#example of remove
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n A {too_expensive.title()} is too expensive for me.")