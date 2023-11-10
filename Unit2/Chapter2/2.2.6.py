class Student:
    def __init__(self, sid, name, grade):
        self.sid = sid
        self.name = name
        self.grade = grade

    def __len__(self):
        return len(self.name)


student = Student(sid=1, name="Alice", grade="A")
print(len(student))
