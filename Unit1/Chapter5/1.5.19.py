for i in range(1, 9 + 1):
    for j in range(1, i + 1):
        product = i * j
        print(f"{j} * {i} = {product}", end="\t")
    print()