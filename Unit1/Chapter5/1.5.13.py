"""
1.5.13  Summation (Odd and Even)
Calculate the sum of all odd and even numbers between 1 and 100 using a for loop
"""

sum_even = 0
sum_odd = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print(sum_even)
print(sum_odd)