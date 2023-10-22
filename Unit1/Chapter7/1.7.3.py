my_list = [1, 2.0, 3, 4.0, True, 'False']


def double():
    i = 0
    while i < len(my_list):
        if type(my_list[i]) == int:
            my_list[i] *= 2
        elif type(my_list[i]) == float:
            my_list[i] *= 2
        i += 1


double()
print(my_list)