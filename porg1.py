class Student:
    college="Aditya"
    def __init__(self,name,rollno,fee):
        self.name=name
        self.rollno=rollno
        self.fee=fee
        
class HostelStudent(Student):
    def __init__(self,room,hfee,name,rollno,fee):
        super().__init__(name,rollno,fee)
        self.room=room
        self.hfee=hfee
    def display_data(self):
        print(self.name,self.rollno,self.fee,self.college,self.room,self.hfee)
class DayscholarStudent(Student):
    def __init__(self,busno,bfee,name,rollno,fee):
        super().__init__(name,rollno,fee)
        self.busno=busno
        self.bfee=bfee
    def display_data(self):
        print(self.name,self.rollno,self.fee,self.college,self.busno,self.bfee)
s1=HostelStudent(207,"80k","subham","1248","70k")
s1.display_data()
s2=DayscholarStudent("402","60k","subham","1248","70k")
s2.display_data()
