invitation = ['Aanchal', 'Lenicka', 'Dad', 'Mom']

invitation.append('Steve')
invitation.insert(0,'Vaclav')
invitation.insert(3,'Benik')

print('Sorry, I can only invite two people.\n')

print(f'Hello, {invitation.pop(0)}, sorry you can\'t come anymore.')
print(f'Hello, {invitation.pop(2)}, sorry you can\'t come anymore.')
print(f'Hello, {invitation.pop(2)}, sorry you can\'t come anymore.')
print(f'Hello, {invitation.pop(2)}, sorry you can\'t come anymore.')
print(f'Hello, {invitation.pop(2)}, sorry you can\'t come anymore.\n')


print(f'Hello,{invitation[0]}, you\'re still invited.')
print(f'Hello,{invitation[1]}, you\'re still invited.\n\n')

del invitation[0]
del invitation[0]

print(invitation)


