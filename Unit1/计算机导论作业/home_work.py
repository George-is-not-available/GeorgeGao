def simple_sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum
num = [10,1,37,19,5,21,7,12]
result = simple_sum(num)
print(result)
