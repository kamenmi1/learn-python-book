filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

birthday = input("Tell me your birthday in format ddmmyy: ")

if birthday in pi_string:
    print("Great job, your bithday is in the PI!")
else:
    print("Sorry your birthday is not in the first million of nu. PI.")

print(pi_string[:52])
print(len(pi_string))