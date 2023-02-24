#Decorator takes in a function, adds some  functionality and returns it.
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner
def ordinary():
    print("I am ordinary")
@make_pretty #Method2 of decorating  --> makepretty(extraordinary)
def extrordinary():
    print("I am extraordinary")

if __name__=='__main__':
    ordinary()
    print('********')
    pretty=make_pretty(ordinary)#Method1 of Decorating  --> giving function as argument
    pretty()
    print('**********')
    extrordinary()
    print('**********')