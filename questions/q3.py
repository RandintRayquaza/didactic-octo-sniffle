# create a class calculator that inherits  multiple parent class  addition ,substraction and multplication create methods 

class Addition:
    def add(self, a, b):
        print(a+b)
    
class Subtraction:
    def sub(self, a, b):
        print(a-b)

class Multiplication:
    def mul(self, a, b):
        print( a * b)

class Calculator(Addition, Subtraction, Multiplication):
    pass

calc = Calculator()
calc.add(10, 5)
calc.sub(10, 5)
calc.mul(10, 5)
