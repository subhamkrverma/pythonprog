class Sbi:
    def __init__(self,name,branch,ifsc):
        self.name=name
        self.branch=branch
        self.ifsc=ifsc
    def display_data(self):
        print(self.name,self.branch,self.ifsc)
    class pnb:
        def __init__(self,branch,ifsc):
            self.branch=branch
            self.ifsc=ifsc
        def display_data(self):
            print(self.branch,self.ifsc)
s1=Sbi("SBI","sabour","SBIN0011805")
s1.display_data()
s2=Sbi.pnb("bhagalpur","PNB000332")
s2.display_data()
        
