class Student:
    def __init__(self, sid, name, grade):
        self.sid = sid
        self.name = name
        self.grade = grade

    def __str__(self):
        return self.name


student1 = Student(sid=1, name="Alice", grade="A")
student2 = Student(sid=2, name="Bob", grade="B")
print(student1)
print(student2)
