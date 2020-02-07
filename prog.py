class Student:
    def __init__(self):
        print("self class")
    def data(self):
        print("super class")
class Hostel(Student):
    def __init__(self):
        super().__init__()
        print("sub class")
s1=Hostel()
