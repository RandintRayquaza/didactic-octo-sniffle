class Bank_account:
  def __init__(self,name ,bal,acc_num ):
    self.name = name
    self.bal = bal
    self.acc = acc_num

  def deposit(self, ammt):
    if ammt > 0:
      self.bal += ammt
      print(f"Bank Account - your balance is {self.bal}")

  def widthraw(self, ammt):
    if ammt > 0 and ammt <= self.bal:
      self.bal -= ammt
      print(f"Bank Account - your balance is {self.bal}")

  def show_balance(self):
    print(f"Bank Account - your balance is {self.bal}")

c1 =Bank_account('Aryan',3884,34878873586438)
c1.deposit(5466)
c1.show_balance()



class savings_bankAccount(Bank_account):
    def widthraw(self, ammt):
      if ammt<=10000:
         self.bal -= ammt
         print(f"Savings Account - your balance is {self.bal}")
    
    def show_balance(self):
      print(f"Savings Account - your balance is {self.bal}")


s1= savings_bankAccount('Aryan',2374862385,34878873586438)
s1.widthraw(5000 )
s1.show_balance()

  
class salary_account(Bank_account):
    def deposit(self, ammt):
      if ammt > 20000:
        self.bal += ammt
        print(f"Salary Account - your balance is {self.bal}")
    
    def show_balance(self):
      print(f"Salary Account - your balance is {self.bal}")

s2= salary_account('Aryan',2374862385,34878873586438)
s2.deposit(5000)
s2.show_balance()