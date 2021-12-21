class bank:
    def __init__(self):
        self.accno=int(input("enter account number"))
        self.name=input("enter account holders name")
        self.type=input("enter account type (c/s)")
        self.bal=int(input("enter balance"))
    def deposit(self,amt):
        self.bal=self.bal+amt
        print("new amount after deposit",self.bal)
    def withdraw(self,amt):
        self.bal=self.bal-amt
        print("new after withdrawal",self.bal)
b1=bank()
d=int(input("enter amount to be deposited"))
b1.deposit(d)
w=int(input("enter amount to be withdrawn"))
b1.withdraw(w)
