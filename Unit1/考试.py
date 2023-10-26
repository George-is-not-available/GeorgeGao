"""1. Recursion List"""


def recursive_list_sum(inputlist):
    total_sum = 0
    for item in inputlist:
        if isinstance(item, list):
            total_sum += recursive_list_sum(item)
        else:
            total_sum += item
    return total_sum


input_list = [1, 2, [3, 4], [5, 6]]
result = recursive_list_sum(input_list)
print(result)

"""2. Polynomial"""


# (1) #
def sum_of_positive_integers(n):
    total_sum = 0
    while n > 0:
        total_sum += n
        n -= 2
    return total_sum


input_value = 6
result = sum_of_positive_integers(input_value)
print(result)


# （2） #
def sum_of_positive_integers(n):
    total_sum = 0
    x = 0

    while n - x > 0:
        total_sum += n - x
        x += 2

    return total_sum


n = 10
result = sum_of_positive_integers(n)
print(result)

"""3.Geometric Sum"""


# (1) #
def harmonic_sum(n):
    if n <= 1:
        return 0.0

    total_sum = 0.0
    for i in range(1, n-1):
        total_sum += 1.0 / i

    return total_sum


n = 7
result = harmonic_sum(n)
print(result)
# (2) #
def geometric_sum(n):
    a = 1
    r = 0.5

    sum_result = a * (1 - r**n) / (1 - r)

    return sum_result


n = 9
result = geometric_sum(n)
print(result)




"""4. Harmonic Sum"""
# (1) #
def harmonic_sum(n):
    if n <= 1:
        return 0

    total_sum = 0.0
    for i in range(1, n + 1):
        total_sum += 1.0 / i

    return total_sum


n = 7
result = harmonic_sum(n)
print(result)
# (2) #

def harmonic_sum(n):
    if n <= 1:
        return 0

    total_sum = 0.0
    for i in range(2, n):
        total_sum += 1 / i

    return total_sum


n = 4
result = harmonic_sum(n)
print(result)

"""5. GCD *"""
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


number1 = 12
number2 = 14

result = gcd(number1, number2)
print(result)

"""6.LCM*"""
def find_lcm(a, b):
    if a > b:
        greater = a
        smaller = b
    else:
        greater = b
        smaller = a
    lcm = greater
    while True:
        if lcm % smaller == 0:
            return lcm
        lcm += greater


number1 = 12
number2 = 14
result = find_lcm(number1, number2)
print(result)

