class Person:
    def __init__(self, name):
        self.__name = name

    def set_name(self, new_value):
        if len(new_value) < 10:
            self.__name = new_value

    def get_name(self):
        return self.__name


person = Person("John")
print(person.get_name())
person.set_name("Alice")
print(person.get_name())
person.set_name("Christopher")
print(person.get_name())
