class Atm(object):

 def __init__(self,atmCardNo , pinNo) :
        self.atmcardnumber=atmCardNo
        self.pinnumber=pinNo


    
 def withDrawl(self):
      print("CashWithdrawl")


 def balance(self):
      print("BalanceEnquiry")

axis = Atm("12345","398374")
print(axis.atmcardnumber)
print(axis.pinnumber)


axis.withDrawl()
axis.balance()