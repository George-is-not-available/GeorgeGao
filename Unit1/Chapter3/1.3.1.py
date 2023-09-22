import math
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
area = math.pi * radius**2
print(f"Circumference: {round(circumference, 2)} units")
print(f"Area: {round(area, 2)} square units")
