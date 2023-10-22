"""
6. Symmetric Difference Pro
Write a function to create a symmetric difference of n sets.
"""


def symmetric_difference_of_sets(sets_list):
    result = sets_list[0].copy()

    for s in sets_list[1:]:
        result = result.symmetric_difference(s)

    return result


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {5, 6, 7, 8}
set4 = {6, 7, 8, 9}

result_difference = symmetric_difference_of_sets([set1, set2, set3, set4])
print(result_difference)