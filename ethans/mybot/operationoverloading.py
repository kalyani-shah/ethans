class A:
    def __init__(self,geta):
        self.a=geta
    def __add__(self,other):
        return self.a*other.a
#op overloading is implemented with help of overriding
ob1= A(10)
ob2= A(200)
print(ob1 + ob2)  #ob1.__add__(ob2)

'''__add__ is mentioned in object class but we're writing again in parent class which is called overriding'''