def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            return "Whoops! cannot divide"
        return func(a, b)
    return inner
@smart_divide  #--> smartdiide(mydiv)
def mydiv(a,b):
    return a/b
#@smart_divide
def mysub(a,b):
    return a-b
if __name__=='__main__':
    print(mydiv(8,9))#mydiv reference to inner
    print('================')
    print(mydiv(8, 0))