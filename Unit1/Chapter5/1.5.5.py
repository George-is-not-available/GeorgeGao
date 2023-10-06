import random


secret_number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        error = abs(secret_number - guess)

        if error == 0:
            print(f"Congratulations! You guessed the correct number, which is {secret_number}.")
            break
        elif error > 50:
            print("Not even close.")
        elif error > 30:
            print("Wrong.")
        else:
            print("Close.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
