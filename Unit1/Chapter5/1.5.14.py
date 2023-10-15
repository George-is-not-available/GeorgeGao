num = int(input("Enter a positive number......"))

index = 0

for i in range(1, num + 1):
    if num % i == 0:
        index += 1

if index == 2:
    print("This is a prime number.")
else:
    print("This is not a prime number.")