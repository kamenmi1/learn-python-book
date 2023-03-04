places_to_see = ['Toronto', 'Zurich', 'Iceland', 'Norway', 'Tokio']

#printing raw list
print(places_to_see)

#printing alphabetically sorted list using sorted function - no sorting is happening to the list
print(sorted(places_to_see))
#proof
print(f'{places_to_see}, still has the same orded as before using sorted function')

# sorted reversed
print(sorted(places_to_see, reverse=True))

# reverse the list 
places_to_see.reverse()
print(places_to_see)

# reversing back to the original state
places_to_see.reverse()
print(places_to_see)

# sorting 
places_to_see.sort()
print(places_to_see)

#sorting reversed
places_to_see.sort(reverse=True)
print(places_to_see)