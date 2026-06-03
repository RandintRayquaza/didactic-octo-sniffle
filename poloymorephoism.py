#it is a process of making an oprator or method to work on one or more oprations 
def demo():
    print("Polymorphism")

var = demo

def demo(a,b):
    return a+b
mid = demo
def demo(a,b,c):
    return a*b*c


print(demo(2,3,4))

print(mid(2,3))

var()


#code eg using class

class Employee:
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        return 5000

class intern(Employee):
    def calculate_salary(self):
        return 2000



sal = [Manager(), intern(),]

for i in sal:
    print(i.calculate_salary())


