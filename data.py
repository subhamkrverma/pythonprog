class Student:
    def __init__(self):
        print("super class")
    def data(self):
        print("super class data method")
class Hostel(Student):
    def __init__(self):
        print("sub class")
        
    
s1=Hostel()
s1.data()
