while True:
    try:
        # Ask the user for a number
        user_input = input("Enter a number (or 'q' to quit): ")

        # Check if the user wants to quit
        if user_input.lower() == 'q':
            break

        # Convert the user input to an integer
        number = int(user_input)

        # Check if the number is a multiple of 10
        if number % 10 == 0:
            print(f"{number} is a multiple of 10.")
        else:
            print(f"{number} is not a multiple of 10.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
