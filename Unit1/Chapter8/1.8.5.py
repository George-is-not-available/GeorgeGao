"""
5. Existence
Write a function to check if a given value is present in a set or not
"""


def check_exist(set_1, value):
    set_1 = list(set_1)
    try:
        set_1.index(value)
    except ValueError:
        print("Value does not exist")
    else:
        print("Value exist")


my_list = {1, 2, 3, 4, 5}
my_value = 6
check_exist(my_list, my_value)