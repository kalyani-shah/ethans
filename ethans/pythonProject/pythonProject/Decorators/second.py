#functions can be passed as arguments to other function

def inc(x):
    return x + 1
def dec(x):
    return x - 1
def operate(fun,num):  #fun <inc,dec> used as argument
    res=fun(num) # --> inc(5)
    return res
if __name__=='__main__':
    print(operate(inc,5))
    print(operate(dec,5))