# Initialize variables for the sums
sum_odd = 0
sum_even = 0

# Initialize a counter
n = 1

while n <= 100:
    if n % 2 == 0:  # Check if n is even
        sum_even += n
    else:
        sum_odd += n
    n += 1

print(f"Sum of even numbers between 1 and 100: {sum_even}")
print(f"Sum of odd numbers between 1 and 100: {sum_odd}")
