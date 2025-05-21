from abstraction import Family
class dady(Family):
    def __init__(self,mony):
        super().__init__(mony)
    def home(self):
        print("dady is back..")
        print(f"I have {self.mony} in my hand")
class mom(Family):
    def home(self):
        print("momy..")
        print(f"ljfs{self.mony}")
class boy(Family):
    def __init__(self, mony,sarts,pent):
        super().__init__(mony)
        self.sarts=sarts
        self.pent =pent
        self.book = 10
    def home(self):
        print("I am home..")
        print(f"I have {self.sarts}and {self.pent}")
        print(f"also i am student so i have {self.book}")

da = dady(122)
da.home()
da.car()
mo = mom(4)
mo.home()
bo = boy(100,"blue","black")
bo.home()