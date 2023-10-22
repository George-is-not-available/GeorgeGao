"""
3. Remove
Write a function to remove all elements from a given set
"""


def remove_set(set_1):
    set_1.clear()
    print(set_1)


my_set = {1, 2, 3, 4, 5, 6}
remove_set(my_set)