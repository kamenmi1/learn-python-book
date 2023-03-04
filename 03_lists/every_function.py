mountains = ['k2','mount everest','nanga parbart','tirich mir', 'denali', 'mount kilimanjaro', 'kongur tagh', 'gonggar mountain']

# all functions that can be done on a list (that I learned in this chapter)

#append - adding new item at the end of a list 
mountains.append('cool mountain')
print(f'{mountains}\n')

#insert - inserting new item at giving index in a list
mountains.insert(1,'not so cool mountain')
print(f'{mountains}\n')

#del - deletes an item from the list - choosen by an index
del mountains[1]
print(f'{mountains}\n')

#pop - pops out an item from the list and still can be used 
print(f'{mountains.pop(0)}, {mountains}\n')
 
#remove - removes an item from a list according to a name of an item
mountains.remove('denali')
print(f'{mountains}\n')

#sort - sorts the list and changes its sorting
mountains.sort()
mountains.sort(reverse=True)
print(f'{mountains}\n')

#sorted - shows how the list will look like when sorted - keeps the original state of the list
print(f'{sorted(mountains)}\n')
print(f'{sorted(mountains, reverse=True)}\n')

#len - gives you an int of lenght of the list
print(f'{len(mountains)}\n')

#reverse - reverse the list - no aplhabetical changes happening 
mountains.reverse()
print(f'{mountains}\n')

mountains.reverse()
print(f'{mountains}\n')




