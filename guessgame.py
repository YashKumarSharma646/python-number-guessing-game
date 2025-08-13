import random
import sys

# Check if user gave a max number as a command-line argument
if len(sys.argv) > 1:
    try:
        max_num = int(sys.argv[1])
        if max_num < 1:
            raise ValueError
    except ValueError:
        print("Please enter a valid positive number as the range limit.")
        sys.exit(1)
else:
    max_num = 10  # Default range

print(f"Welcome to the Guessing Game! (Range: 1 to {max_num})")
print("Type 'exit' anytime to quit.\n")

while True:
    user_input = input(f"Enter a number between 1 and {max_num}: ")

    if user_input.lower() == "exit":
        print("Thanks for playing! Goodbye.")
        sys.exit(0)  # Clean exit

    try:
        guess = int(user_input)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess < 1 or guess > max_num:
        print(f"Choose a number within the range 1 to {max_num}.")
        continue

    random_num = random.randint(1, max_num)

    if guess == random_num:
        print("Genius! You guessed it right!")
    else:
        print(f"No luck! The correct number was {random_num}. Try again!")


