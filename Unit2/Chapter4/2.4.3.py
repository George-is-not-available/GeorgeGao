class Exam:
    def __init__(self, start_time, end_time, points):
        self.start_time = start_time
        self.end_time = end_time
        self.points = points

    def __str__(self):
        print(f"Exam: Start Time - {self.start_time}, End Time - {self.end_time}, Points - {self.points}")


class Test(Exam):
    def __init__(self, points=10):
        super().__init__(start_time=None, end_time=None, points=points)

    def __str__(self):
        print(f"Test: Points - {self.points}")
