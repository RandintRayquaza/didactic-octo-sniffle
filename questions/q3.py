# create a class calculator that inherits  multiple parent class  addition ,substraction and multplication create methods 

class Addition:
    def add(self, a, b):
        print(a+b)
    
class Subtraction:
    def sub(self, a, b):
        print(a-b)

class Multiplication:
    def multi(self, a, b):
        print( a * b)

class Calculator(Addition, Subtraction, Multiplication):
    pass

calc = Calculator()
calc.add(10, 5)
calc.sub(10, 5)
calc.multi(10, 5)




#uisng init method

class Addition: 
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)

class Subtraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sub(self):
        print(self.a - self.b)

class Multiplication:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def multi(self):
        print(self.a * self.b)

class Calculator(Addition, Subtraction, Multiplication):
    def __init__(self, a, b):
        Addition.__init__(self, a, b)
        Subtraction.__init__(self, a, b)
        Multiplication.__init__(self, a, b)


calc = Calculator(10, 5)
calc.add()
calc.sub()
calc.multi()

