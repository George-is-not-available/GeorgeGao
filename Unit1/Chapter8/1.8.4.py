"""
4. Max and Min
Write a function to find the maximum and minimum values in a set
"""


def find_max_min(set_1):
    max_set1 = max(set_1)
    min_set1 = min(set_1)
    print(f"Max Value: {max_set1}, Min set: {min_set1}")


my_set = {4, 5, 1, 3, 9, 5, 4, 1, 3}
find_max_min(my_set)