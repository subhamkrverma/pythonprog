class Student:
    def __init__(self):
        print("super class")
    def data(self):
        print("super class data method")
class Hostel(Student):
    def __init__(self):
        super().__init__()
    
s1=Hostel()
