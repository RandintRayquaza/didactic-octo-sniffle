
class Bank:
    def __init__(self, bal, accno):
        self.__bal = bal
        self.__accno = accno


c1 = Bank(34000, 37848)
print(c1.__bal)
    