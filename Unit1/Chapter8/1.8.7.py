def find_third_largest_num(set1):
    set1 = list(set1)
    set1.sort(reverse=True)
    print(set1[2])


my_set = {9, 5, 6, 7, 8, 1}
find_third_largest_num(my_set)