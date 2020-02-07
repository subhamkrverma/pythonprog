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
        print(self.room,self.hfee,self.name,self.rollno,self.fee,self.college)
s1=HostelStudent(207,"80k","subham","1248","70k")
s1.display_data()
