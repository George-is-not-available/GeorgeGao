"""
2. Subset
Write a function to check if a set is a subset of another set
"""


def subset_check(set_1, set_2):
    set_3 = set_1.difference(set_2)
    if set_3 == set():
        print(f"{set_1} is a subset of {set_2}.")
    set_4 = set_2.difference(set_1)
    if set_4 == set():
        print(f"{set_2} is a subset of {set_1}")


my_set_1 = {1, 2, 3, 4, 5}
my_set_2 = {1, 2, 3}
subset_check(my_set_1, my_set_2)