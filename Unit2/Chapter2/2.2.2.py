class Student:
    def __init__(self, sid, name, grade):
        self.sid = sid
        self.name = name
        self.grade = grade

    def __del__(self):
        print(f"Student {self.name} has been deleted")


student1 = Student(sid=1, name="Alice", grade="A")
student2 = Student(sid=2, name="Bob", grade="B")


del student1
del student2

