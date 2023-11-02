def gcd(num1, num2):
    num_process = [num1, num2]
    cd_list = []
    i = 1
    while i <= max(num_process):
        if num1 % i == 0 and num2 % i == 0:
            cd_list.append(i)
            i += 1
        else:
            i += 1
    return cd_list[len(cd_list) - 1]


my_num_1 = 12
my_num_2 = 14
print(gcd(my_num_1, my_num_2))