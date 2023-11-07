"""
（1）打印数字1-5

for value in range(1,6):
    print(value)

输出结果：1、2、3、4、5
（2）创建数字列表，使用“list()”函数将结果转换为列表格式

numbers = list(range(1,6))
print(numbers)

输出结果：[1, 2, 3, 4, 5]
（3）打印1-10内的所有偶数

numbers = list(range(2,11,2))
print(numbers)

输出结果：[2, 4, 6, 8, 10]
（4）创建一个1-10的平方数字列表

squares = [ ] # 先创建一个用于存储计算值的空列表.
for value in range(1,11): # 遍历1-10的所有值.
    square = value**2 # 计算当前平均值，并将结果存储在square中.
    squares.append(square) # 将计算结果存储在空列表中.
print(squares)

输出结果：[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

备注：在Python中两个星号（**）表示乘方运算。

"""