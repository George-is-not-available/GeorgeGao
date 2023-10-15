def create_multiply_table(a):
    table = ""
    for i in range(1, a + 1):
        for j in range(1, i + 1):
            product = i * j
            table += f"{j} * {i} = {product}\t"
        table += "\n"
    return table



row = int(input("Enter rows: "))
table_str = create_multiply_table(row)
print(table_str)

