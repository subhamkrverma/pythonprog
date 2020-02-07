class Student:
    college="Aditya"
    def __init__(self,name):
        self.name=name
    def setmarks(self,s1,s2,s3):
        self.s1=s1
        self.s2=s2
        self.s3=s3
    def get_total(self):
        return self.s1+self.s2+self.s3
    
   
    @staticmethod
    def get_avg(total):
       return total/3
    def display_data(self,total,avg):
        print(self.name,self.s1,self.s2,self.s3,total,avg)
        
obj1=Student("siva")
obj1.setmarks(76,87,98)
total=obj1.get_total()
avg=Student.get_avg(total)
obj1.display_data(total,avg)
