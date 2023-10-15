num = int(input("Enter a positive number......"))
print(f"{num} =", end=' ')
divisor = 2

for divisor in range(2, num + 1):
    while num >= 2:
        if num % divisor == 0:
            print(divisor, sep='1', end=' ')
            num //= divisor
        else:
            divisor += 1
    break