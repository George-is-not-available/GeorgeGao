# Initial amount in Xiaohong's account
initial_balance = 200000000  # ￥200 million

# Initial number of months
months = 0

# While her balance is greater than or equal to ￥10
while initial_balance >= 10:
    # Half her balance every month
    initial_balance /= 2
    months += 1

# Print the result
print(f"It took {months} months for Xiaohong's assets to fall below ￥10.")
print(f"At that time, her assets were worth ￥{initial_balance:.2f}.")
