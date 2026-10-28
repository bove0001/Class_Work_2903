# import needed modules
import random
import string 

# build the banner text
banner_message = '* AWESOME Password Generator PROGRAM *'
stars = '*' * len(banner_message)  # stars match banner width
# print the banner
print(stars)
print(banner_message)
print(stars)

letters = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# ask user for length
length_input = input('Enter password length: ')

# check for vaild positive number
if length_input.isdigit() and int(length_input) > 0:
    password_length = int(length_input)
else:
    # fall back to default
    print('Invalid number, using 16.')
    password_length = 16


# start with empty password
password = ''

# loop once per character
for letter in range(password_length):
    random_letter = random.choice(letters)  # pick a random letter
    password = password + random_letter  # add it to password

# show the final pasword
print('Your password is ' + password)

