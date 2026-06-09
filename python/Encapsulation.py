
# class Bank:
#     def __init__(self, bal, accno):
#         self.__bal = bal
#         self.__accno = accno
#     def get_bal(self):
#         return self.__bal
    
#     def __validate_ammt(self,ammt):
#         return ammt>0
        


#     def set_bal(self,ammt):
#         if self.__validate_ammt(ammt):
#             self.__bal = ammt
#             print(f'New amount{self.__bal}')
        

# c1 = Bank(23347,3473)
# c1.__bal = 90000
# c1.set_bal(40000)
# print(c1.get_bal())







class student:
    def __init__(self,name,marks):
        self.namm = name
        self.__marks = marks
    def  set_marks(self,new):
        if new >0:
            self.__marks=+new

    def get_marks(self):
        return self.__marks
    
s1 = student('Aryan',89)
print(s1.get_marks())
s1.set_marks(90)
print(s1.get_marks())


# create a class employee private attribute: slaary methods set_slaary(ammt) validte slaary>0
#get_Salary() slary



class employee:
    def __init__(self,name,salary):
        self.name = name 
        self.__salary  = salary

    def set_salary(self,ammt):
        if ammt > 0:
            self.__salary = ammt
            print(f'New salary is {self.__salary}')
    def get_salary(self):
        return self.__salary


e1= employee('Aryan',10000)
print(e1.get_salary())
e1.set_salary(12000)
print(e1.get_salary())
