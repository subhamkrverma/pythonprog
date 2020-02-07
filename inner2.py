class Student:
    def __init__(self,name,roll,phno,ram,pro,hd):
        self.name=name
        self.roll=roll
        self.phno=phno
        self.lap=self.laptop(ram,pro,hd)
    def display_data(self):
        print(self.name,self.roll,self.phno)
        self.lap.display_data()
    class laptop:
        def __init__(self,ram,pro,hd):
            self.ram=ram
            self.pro=pro
            self.hd=hd
        def display_data(self):
            print(self.ram,self.pro,self.hd)
s1=Student("siva","1234","987654321","8gb","17","1TB")
s1.display_data()
