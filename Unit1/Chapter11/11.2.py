def polynomial(a):
    i = 0
    output = 0
    while a - i >= 0:
        output += (a - i)
        i += 2
    return output


my_num = 10
print(polynomial(my_num))