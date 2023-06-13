#reading from a file

with open('pi_digits.txt') as file_object:
    contents = file_object.read()

# print(contents.rstrip())

filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())


# save the lines into the variable outside, because the file will be closed.
with open(filename) as file_object:
    lines = file_object.readlines()

print(f"Those are all lines: {lines}")

for line in lines:
    print(line)
    
# print(file_object.read()) # can't be read, because the file is arleady closed.

