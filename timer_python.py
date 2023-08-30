import time

print("Countdown Timer")

try:
    seconds = int(input("Enter the number of seconds: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    if seconds < 0:
        print("Please enter a positive number.")
    else:
        print(f"Timer set for {seconds} seconds.")
        while seconds > 0:
            print(seconds)
            time.sleep(1)
            seconds -= 1
        print("Time's up!")
