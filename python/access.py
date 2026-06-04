#public acces specfire

class Studnets:
    def __init__(self,name):
        self.name = name
        print(self.name)
s1 = Studnets('Aryan') 

print(s1.name)


#protected access 

class Devloper:
    def __init__(self,name,salary):
        self.name = name 
        self._salary  = salary
      
        

        print(self._salary)

d1= Devloper('Aryan',10000)
print(d1._salary)



#Real private specfire

# class employee:
#     def __init__(self,name,salary):
#         self.name = name 
#         self.__salary  = salary

#         print(self.__salary)

# e1= employee('Aryan',10000)
# print(e1.self.__salary)


class Bank:
    def __init__(self, bal, accno):
        self.__bal = bal
        self.__accno = accno


c1 = Bank(34000, 37848)
print(c1._Bank__bal)
    
