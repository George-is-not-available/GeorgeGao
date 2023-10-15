height = int(input("Enter height: "))

for i in range(1, height, 2):
    spaces = (height - i) // 2
    print(" " * spaces + "*" * i)

print("*" * height)

for i in range(height - 2, 0, -2):
    spaces = (height - i) // 2
    print(" " * spaces + "*" * i)