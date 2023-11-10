class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color


apple = Fruit("Apple", "Red")
orange = Fruit("Orange", "Orange")
watermelon = Fruit("Watermelon", "Green")
print(f"The color of the {apple.name.lower()} is {apple.color}.")
print(f"The color of the {orange.name.lower()} is {orange.color}.")
print(f"The color of the {watermelon.name.lower()} is {watermelon.color}.")
