# sorting cars in alphabetical order - sorting the list completely, can't be taken back

cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

# reversed 
cars.sort(reverse=True)
print(cars)

# sorted function - shows how the list will look like sorted without doing anything to the list
cars = ['bmw','audi','toyota','subaru']

print(f'\n\nHere is the original list: {cars}\n')
print(f'Here is the sorted list: {sorted(cars)}\n')
print(f'Here is the original list again: - no change happened to it - {cars}')

# sorted can also take an argument for reverse the sorting 
print(sorted(cars,reverse=True))

# printing a list in reverse order
cars = ['bmw','audi','toyota','subaru']

print(cars)
cars.reverse()
print(cars)

# lenght of the list 

cars = ['bmw','audi','toyota','subaru']
print(len(cars))