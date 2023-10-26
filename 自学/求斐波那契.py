# 输入要计算的斐波那契数列的长度
n = int(input("请输入斐波那契数列的长度: "))

# 初始化前两个斐波那契数
fibonacci_sequence = [0, 1]

# 使用循环计算斐波那契数列
for i in range(2, n):
    next_fibonacci = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
    fibonacci_sequence.append(next_fibonacci)

# 输出斐波那契数列
print("斐波那契数列:")
for number in fibonacci_sequence:
    print(number)
