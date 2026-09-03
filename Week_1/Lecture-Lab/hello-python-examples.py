print('Hello capstone!')

# Variables
school = 'MCTC'
gpa = 3.7
students_in_class = 22

# if-statements
if gpa == 4:
    print('WOW!')
elif gpa > 3:
    print('Awesome!')
else:
    print('Cool!')

# if-elif-else

# lists
schools = ['MCTC', 'DCTC', 'North Hennepin Technical College']
if 'MCTC' in schools:  # check membership with 'in'
    print('MCTC is one of the schools in the list')

schools.sort()  # sort list alphabetically, in place
print(schools)
schools.append('Century College')  # add item to end of list
print(schools)

schools.reverse()  # reverse list in place, returns None
print(schools)
# in operator

# strings
class_name = 'Software Development Capstone'
print(class_name.upper())        # convert to uppercase
print(len(class_name))           # length of string
print(class_name.split())        # split into list of words by whitespace
print(class_name.split('o'))     # split by the letter 'o'

if 'Capstone' in class_name:  # substring check
    print('This must be the capstone')

# loops - for loops over range
for x in range(10):  # loop from 0 to 9
    print(x)

for letter in school:  # loop over each character in string
    print(letter * 10)  # repeat character 10 times

data = [0] * 10          # list of 10 zeros
print(data)

more_data = [None] * 10  # list of 10 Nones
print(more_data)

# while loops

# name = input('Enter your name: ')
# while not name:
#     print('Please enter at least one character ')
#     name = input('Enter your name: ')

# True and False and None

start_of_semester = True
winter = False

if winter:
    print('brr!')
else:
    print('it is not winter')

# Dictionaries
class_codes = {2905: 'Capstone', 2560: 'Web', 2545: 'Java'}  # key: class code, value: class name

print(class_codes[2560])  # access value by key

for code in class_codes:  # loop over keys by default
    print(code)
    print(class_codes[code])

for code, name in class_codes.items():  # loop over key-value pairs
    print('The class code is ' + str(code) + ' and the name is ' + name)

for code, name in class_codes.items():  # same loop, using f-string formatting
    print(f'The class code is {code} and the name is {name}')

# Slicing strings, lists
schools = ['MCTC', 'DCTC', 'North Hennepin Technical College']
first_two = schools[:2]  # first two elements
print(first_two)

last_school = schools[-1]  # last element
print(last_school)
last_two_schools = schools[-2:]  # last two elements
print(last_two_schools)

school_name = 'Minneapolis Community and Technical College'
city = school_name[:11]  # first 11 characters
print(city)

# File IO
with open('datafile.txt') as f:  # open file for reading
    print(f.read())

with open('schools.txt', 'w') as f:  # open file for writing (overwrites)
    f.writelines(schools)  # write list items to file (no newlines added)

# Functions
def get_name():
    print('Hello, please enter your name!')
    name = input('Your name is: ')  # get user input
    return name
name = get_name()