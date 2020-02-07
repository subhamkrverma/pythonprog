class Student:
    def __init__(self,name,roll,phno,ram,pro,hd,model,mram,proc):
        self.name=name
        self.roll=roll
        self.phno=phno
        self.lap=self.laptop(ram,pro,hd)
        self.mob=self.mobile(model,mram,proc)
    def display_data(self):
        print(self.name,self.roll,self.phno)
        self.lap.display_data()
        self.mob.display_data()
    class laptop:
        def __init__(self,ram,pro,hd):
            self.ram=ram
            self.pro=pro
            self.hd=hd
        def display_data(self):
            print(self.ram,self.pro,self.hd)
    class mobile:
            def __init__(self,model,mram,proc):
                self.model=model
                self.mram=mram
                self.proc=proc
            def display_data(self):
                print(self.model,self.mram,self.proc)
s1=Student("siva","1234","987654321","8gb","17","1TB","samsung","3GB","Quadcore")
s1.display_data()
