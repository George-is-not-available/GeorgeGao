import random


secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number, which is {secret_number}.")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if attempts == max_attempts and guess != secret_number:
    print(f"Sorry, you've reached the maximum number of attempts. The correct number was {secret_number}.")
