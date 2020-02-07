class Student:
    college="Aditya"
    def __init__(self,name):
        self.name=name
    def set_values(self,n,coll):
        self.name=n
    def display_data(self):
        print(self.name,Student.college)

    @classmethod
    def set_class(cls,coll,name):
        cls.college=coll
        cls.name=name
        
obj1=Student("siva")
obj1=Student("shiva")
obj1.set_class("Aditya_group","sshhiivvaa")
obj1.display_data()
obj2=Student("subham")
obj2.display_data()

        

