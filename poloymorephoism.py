#it is a process of making an oprator or method to work on one or more oprations 
def demo():
    print("Polymorphism")

def demo(a,b):
    return a+b
mid = demo
def demo(a,b,c):
    return a*b*c


print(demo(2,3,4))

print(mid(2,3))