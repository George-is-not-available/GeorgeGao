class Student:
    def __init__(self, sid, name, grade):
        self.sid = sid
        self.name = name
        self.grade = grade

    def __le__(self, other):
        return self.grade <= other.grade



student1 = Student(sid=1, name="Alice", grade="A")
student2 = Student(sid=2, name="Bob", grade="B")


print(student1 <= student2)
print(student1 > student2)
print(student1 == student2)
