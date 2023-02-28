name = 'Steve'

name_white_spaces_added = '\tSteve\n'

print('print name:\n', name)
print('print name with all the adde whitespace:\n', name_white_spaces_added)

print('remove right whitespace:\n', name_white_spaces_added.rstrip())
print('remove left whitespace: \n', name_white_spaces_added.lstrip())
print('remove both side whitespaces: \n', name_white_spaces_added.strip())