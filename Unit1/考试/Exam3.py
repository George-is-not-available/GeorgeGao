"""1"""


def print_narcissistic_number():
    for number in range(100, 1000):
        digit1 = number // 100
        digit2 = (number // 10) % 10
        digit3 = number % 10
        if number == digit1 ** 3 + digit2 ** 3 + digit3 ** 3:
            print(number)


print_narcissistic_number()
"""2"""


def print_narcissistic_number():
    for number in range(100, 1000):
        digit1 = number // 100
        digit2 = (number // 10) % 10
        digit3 = number % 10

        # Check if it's a narcissistic number
        if number == digit1 ** 3 + digit2 ** 3 + digit3 ** 3:
            print(number)


print_narcissistic_number()
"""3"""


def find_sum_of_3(num_list):
    num_list.sort()
    result = set()
    for i in range(len(num_list) - 2):
        if i == 0 or (i > 0 and num_list[i] != num_list[i - 1]):
            left, right = i + 1, len(num_list) - 1
            while left < right:
                total = num_list[i] + num_list[left] + num_list[right]
                if total == 0:
                    result.add((num_list[i], num_list[left], num_list[right]))
                    while left < right and num_list[left] == num_list[left + 1]:
                        left += 1
                    while left < right and num_list[right] == num_list[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
    return list(result)


input1 = [-1, 0, 1, 2, -1, -4]
output1 = find_sum_of_3(input1)
print(output1)

input2 = [-1, 0, 1, 2, -1, -4, 0, 2, 0, 4, -4, -2, -1, 2]
output2 = find_sum_of_3(input2)
print(output2)

"""4"""
def max_product(num_list: list) -> int:
    if len(num_list) < 3:
        raise ValueError("Input list should contain at least 3 numbers.")
    num_list.sort()
    max_ = max(num_list[-1] * num_list[-2] * num_list[-3], num_list[0] * num_list[1] * num_list[-1])
    return max_


input1 = [1, 2, 3]
output1 = max_product(input1)
print(output1)

input2 = [1, 2, -3, -3, 0]
output2 = max_product(input2)
print(output2)
