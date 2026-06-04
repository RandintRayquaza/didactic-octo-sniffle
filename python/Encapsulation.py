
class Bank:
    def __init__(self, bal, accno):
        self.__bal = bal
        self.__accno = accno
    def get_bal(self):
        return self.__bal
    
    def __validate_ammt(self,ammt):
        return ammt>0
        


    def set_bal(self,ammt):
        if self.__validate_ammt(ammt):
            self.__bal = ammt
            print(f'New amount{self.__bal}')
        

c1 = Bank(23347,3473)
c1.__bal = 90000
c1.set_bal(40000)
print(c1.get_bal())


