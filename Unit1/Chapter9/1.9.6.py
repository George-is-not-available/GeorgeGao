def join_string(str1, list1):
    amount = len(list1)
    for i in range(1, amount):
        list1.insert(i * 2 - 1, str1)
    list1 = ''.join(list1)
    return list1


my_str = '123'
my_list = ['a', 'b', 'c', 'd']
print(join_string(my_str, my_list))