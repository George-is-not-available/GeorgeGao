"""
1. Symmetric Difference
In mathematics, the symmetric difference of 2 sets, also known as the disjunctive union and set sum,
is the set of elements which are in either of the sets, but not in their intersection
For example, the symmetric difference of the sets {1,2,3} and {3,4} is {1,2,4}
Write a function to create a symmetric difference of 2 sets.
"""


def sym_difference(set1, set2):
    set3 = set1.difference(set2)
    set4 = set2.difference(set1)
    set5 = set3.union(set4)
    print(f"Symmetric difference of set {set1} and {set2} is: {set5}")


my_set_1 = {1, 2, 3, 4}
my_set_2 = {3, 4, 5}
sym_difference(my_set_1, my_set_2)