class Student:
    college="Aditya"
    def __init__(self,name):
        self.name=name
    def set_values(self,n,coll):
        self.name=n
        Student.college=coll
    def display_data(self):
        print(self.name,self.college)
        
obj1=Student("siva")
obj1.set_values("Siva","Aditya_group")
obj1.display_data()
obj2=Student("subham")
obj2.display_data()
