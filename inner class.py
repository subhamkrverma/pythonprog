class Student:
    def __init__(self,name,roll,phno):
        self.name=name
        self.roll=roll
        self.phno=phno
    def display_data(self):
        print(self.name,self.roll,self.phno)
    class laptop:
        def __init__(self,ram,pro,hd):
            self.ram=ram
            self.pro=pro
            self.hd=hd
        def display_data(self):
            print(self.ram,self.pro,self.hd)
s1=Student("siva","1234","987654321")
s1.display_data()
lap1=Student.laptop("8gb","17","1TB")
lap1.display_data()

        

        
