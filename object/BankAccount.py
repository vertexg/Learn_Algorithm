class BankAccount:
  def __init__(self,bankName,ownerName,savings):
    self.bankName = bankName
    self.ownerName = ownerName
    self.savings = savings

  def  depositMoney(self, depositAmount):
    if self.savings <= 20000:
      self.savings += depositAmount -100
    else:
       self.savings += depositAmount
    return int(self.savings)
  
  def  withdrawMoney(self,withdrawAmount):
    Maxwithdraw = self.savings * 0.2
    if withdrawAmount >  Maxwithdraw:
        withdrawAmount =  Maxwithdraw
    self.savings -= withdrawAmount
    return int(self.savings)
  
  def pastime(self, days):
        return self.savings + (days * 0.25)

user1 = BankAccount("Chase", "Claire Simmons", 30000)
print(user1.withdrawMoney(2000))
print(user1.depositMoney(10000))
print(user1.pastime(93))

user2 = BankAccount("Bank Of America", "Remy Clay", 10000)
print(user2.withdrawMoney(5000))
print(user2.depositMoney(12000))
print(user2.pastime(505))
