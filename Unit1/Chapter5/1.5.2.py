while True:
    try:
        age = int(input("Please enter your age (or type '0' to exit): "))


        if age == 0:
            break


        if age < 3:
            ticket_price = 0
        elif 3 <= age <= 12:
            ticket_price = 10
        else:
            ticket_price = 15
        print(f"The cost of your movie ticket is ${ticket_price}")
    except ValueError:
        print("Invalid input. Please enter a valid age.")

print("Thank you for using our movie ticket calculator!")
