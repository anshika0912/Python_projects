import random
import string

print("Password Generator")

length = int(input("Enter the length of the password: "))

if length <= 0:
    print("Password length must be a positive number.")
else:
    password = ''
    characters = string.ascii_letters + string.digits + string.punctuation

    for _ in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)
