class A:
    def __init__(self):
        self.X = 1
        self.Y = 2
        self.Z = 3

    def get_X(self):
        print(self.X)


class B(A):
    def get_Y(self):
        print(self.Y)


class C(B):
    def get_Z(self):
        print(self.Z)


# 创建实例
a = A()
b = B()
c = C()

# 解释每个对象可以调用哪些实例方法

# 对象 'a'（类 'A' 的实例）
# - 可以调用 get_X()，因为它在类 'A' 中被定义。
# - 不能调用 get_Y() 和 get_Z()，因为它们在类 'A' 中未定义。
a.get_X()  # 输出：1

# 对象 'b'（类 'B' 的实例）
# - 可以调用 get_X()，因为它是从类 'A' 继承的。
# - 可以调用 get_Y()，因为它在类 'B' 中被定义。
# - 不能调用 get_Z()，因为它在类 'B' 中未定义。
b.get_X()  # 输出：1
b.get_Y()  # 输出：2

# 对象 'c'（类 'C' 的实例）
# - 可以调用 get_X()，因为它是从类 'A' 继承的。
# - 可以调用 get_Y()，因为它是从类 'B' 继承的。
# - 可以调用 get_Z()，因为它在类 'C' 中被定义。
c.get_X()  # 输出：1
c.get_Y()  # 输出：2
c.get_Z()  # 输出：3
