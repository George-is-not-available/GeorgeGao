try:
    num = int(input("Enter a positive integer: "))

    if num <= 1:
        print("Not a prime number.")
    elif num == 2:
        print("It's a prime number.")
    else:
        is_prime = True
        divisor = 2

        while divisor * divisor <= num:
            if num % divisor == 0:
                is_prime = False
                break
            divisor += 1

        if is_prime:
            print("It's a prime number.")
        else:
            print("Not a prime number.")

except ValueError:
    print("Invalid input. Please enter a positive integer.")
