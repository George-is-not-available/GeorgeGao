class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def study(self, hours):
        print(f"{self.name} is studying for {hours} hours.")

    def take_exam(self):
        print(f"{self.name} is taking an exam.")

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# Create two instances of the Student class
student1 = Student("Alice", 18, "A")
student2 = Student("Bob", 17, "B")

# Print attributes and call methods for each student
print("Student 1:")
student1.display_info()
student1.study(3)
student1.take_exam()

print("\nStudent 2:")
student2.display_info()
student2.study(4)
student2.take_exam()
