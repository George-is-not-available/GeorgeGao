def add_zero(input_list):
    index = 0
    while index < len(input_list):
        input_list.insert(index + 1, 0)
        index += 2
    return input_list


# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = add_zero(my_list)
print(result)