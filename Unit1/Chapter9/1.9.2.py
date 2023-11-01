def reverse_string(string_1):
    string_1 = list(string_1)
    new_string = list()

    for i in range(len(string_1) - 1, -1, -1):
        new_string.append(string_1[i])

    new_string = ''.join(new_string)
    return new_string


my_str = "helloworld"
print(reverse_string(my_str))