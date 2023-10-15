def print_multiply_table(a):
    for i in range(1, a + 1):
        for j in range(1, i + 1):
            product = i * j
            print(f"{j} * {i} = {product}", end="\t")
        print()


row = int(input("Enter rows......"))
print_multiply_table(row)