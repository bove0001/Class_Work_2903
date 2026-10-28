import random
import string 

banner_message = '* AWESOME Password Generator PROGRAM *'
stars = '*' * len(banner_message)
print(stars)
print(banner_message)
print(stars)

letters = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

length_input = input('Enter password length: ')

if length_input.isdigit() and int(length_input) > 0:
    password_length = int(length_input)
else:
    print('Invalid number, using 16.')
    password_length = 16


password = ''

for letter in range(password_length):
    random_letter = random.choice(letters)
    password = password + random_letter

print('Your password is ' + password)

