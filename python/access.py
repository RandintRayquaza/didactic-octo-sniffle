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

c1= Devloper('Aryan',10000)
print(c1._salary)



#Real private specfire

class employee:
    def __init__(self,name,salary):
        self.name = name 
        self.__salary  = salary

        print(self.__salary)

d1= employee('Aryan',10000)
print(d1.self.__salary)



