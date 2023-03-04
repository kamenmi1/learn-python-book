invitation = ['Aanchal', 'Lenicka', 'Dad', 'Mom']

cant_make_it = invitation.pop(0)

print(f'Sadly, {cant_make_it}, Can\'t make it to the dinner.')
print(f'Hello, {invitation[0]}, I would like to invite you to dinner.')
print(f'Hello, {invitation[1]}, I would like to invite you to dinner.')
print(f'Hello, {invitation[2]}, I would like to invite you to dinner.')

print(invitation)

invitation.insert(0,'Steve_the_Plant')

print(f'Hello, {invitation[0]}, I would like to invite you to dinner.')
print(f'Hello, {invitation[1]}, I would like to invite you to dinner.')
print(f'Hello, {invitation[2]}, I would like to invite you to dinner.')
print(f'Hello, {invitation[3]}, I would like to invite you to dinner.')

print(invitation)