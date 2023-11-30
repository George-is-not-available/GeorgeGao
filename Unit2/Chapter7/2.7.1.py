#  __init__.py

from equation.conic.ellipse import Circle
# test.py

from equation import Circle, Ellipse

# 创建 Circle 的实例
circle = Circle(radius=5)

# 测试 Circle 中的方法
print("Circle 面积:", circle.calculate_area())
print("Circle 周长:", circle.calculate_circumference())

# 创建 Ellipse 的实例
ellipse = Ellipse(semi_major_axis=8, semi_minor_axis=5)

# 测试 Ellipse 中的方法
print("Ellipse 面积:", ellipse.calculate_area())
print("Ellipse 周长:", ellipse.calculate_circumference())

