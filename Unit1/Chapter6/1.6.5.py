def create_diamonds(a):
    diamond = []
    for i in range(1, a, 2):
        spaces = (a - i) // 2
        diamond.append(" " * spaces + "*" * i)

    diamond.append("*" * a)

    for i in range(a - 2, 0, -2):
        spaces = (a - i) // 2
        diamond.append(" " * spaces + "*" * i)

    return "\n".join(diamond)


height = int(input("Enter height: "))
diamond_str = create_diamonds(height)
print(diamond_str)