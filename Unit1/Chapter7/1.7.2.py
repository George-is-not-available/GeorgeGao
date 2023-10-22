list_num = [1, 3, 4, 3, 7, 3, 9, 8, 6, 3]

i = 0
while i <= len(list_num):
    print(f"index of 3 is:{list_num.index(3)}")
    if list_num[i] == 3:
        list_num.pop(i)
    i += 1

print(list_num)