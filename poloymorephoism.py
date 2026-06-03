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


#one more 

class A:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a

obj1 = A(10)
obj2 = A(20)
print(obj1 + obj2)

#explanation of above code
#In the above code, we have defined a class A with an __init__ method that initializes an instance variable a. We have also defined the __add__ method, which is a special method in Python that allows us to use the + operator to add two objects of class A together. When we create two objects of class A, obj1 and obj2, with values 10 and 20 respectively, we can use the + operator to add them together. The __add__ method takes the other object as an argument and returns the sum of the a values of both objects. In this case, it will return 30, which is the sum of 10 and 20.