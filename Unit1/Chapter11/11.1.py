def sum_recursion(a):
    sum_of_list = 0
    i = 0
    while i <= len(a) - 1:
        if type(a[i]) == list:
            sum_of_list_inside = 0
            for element in a[i]:
                sum_of_list_inside += element
            sum_of_list += sum_of_list_inside
            i += 1
            continue
        sum_of_list += a[i]
        i += 1
    return sum_of_list


my_list = [1, 2, [3, 4], [5, 6]]
print(sum_recursion(my_list))