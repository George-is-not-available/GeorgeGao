try:
    num = int(input("Enter a positive integer: "))

    if num <= 1:
        print("Factorization is not possible for numbers less than or equal to 1.")
    else:
        print(f"{num} =", end=" ")

        divisor = 2

        while num > 1:
            if num % divisor == 0:
                print(divisor, end=" ")
                num //= divisor
            else:
                divisor += 1

        print()

except ValueError:
    print("Invalid input. Please enter a positive integer.")
