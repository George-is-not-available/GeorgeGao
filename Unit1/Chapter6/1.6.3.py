def create_diamonds(a):
    for i in range(1, a, 2):
        spaces = (a - i) // 2
        print(" " * spaces + "*" * i)

    print("*" * a)

    for i in range(a - 2, 0, -2):
        spaces = (a - i) // 2
        print(" " * spaces + "*" * i)


height = int(input("Enter height: "))
create_diamonds(height)