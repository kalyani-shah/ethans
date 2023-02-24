import mymod
@mymod.smartdiv
def div(a,b):
    return a/b
@mymod.smartdiv
def sub(a,b):
    return a-b
if __name__=='__main__':
    print ('After Decorating Method2:',div(5,9))
    print ('After Decorating Method2:',sub(-5,9))