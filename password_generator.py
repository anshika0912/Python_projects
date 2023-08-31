import random  # Importing the 'random' module to generate random values.
import string # Importing the 'string' module to access character sets like ascii_letters, digits, and punctuation.

print("Password Generator") # Printing a message to indicate the start of the password generator.

length = int(input("Enter the length of the password: "))  # Taking user input for the desired length of the password.

if length <= 0: # Checking if the entered length is a valid positive number.
    print("Password length must be a positive number.")
else:
    password = ''     # Initializing an empty string to store the generated password.
    characters = string.ascii_letters + string.digits + string.punctuation   # Creating a character set by combining letters (both cases), digits, and punctuation.

    for _ in range(length):   # Generating the password by randomly selecting characters from the 'characters' set.
        password += random.choice(characters)

    print("Generated Password:", password)
