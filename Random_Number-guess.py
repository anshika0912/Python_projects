import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Number of attempts the player has
attempts = 0

# Game loop
while True:
    # Take input from the player
    guess = int(input("Your guess: "))
    
    # Increment the number of attempts
    attempts += 1
    
    # Compare the guess with the random number
    if guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
        break  # Exit the loop when the correct number is guessed

print("Thanks for playing!")
