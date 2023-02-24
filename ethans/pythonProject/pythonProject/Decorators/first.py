#FUNCTION IS ALSO AN OBJECT IN PYTHON

def myfirst(msg):
    print('Hi',msg)

if __name__=='__main__':
    myfirst('good evening')
    second = myfirst  #myfirst is used as variable here
    second('good morning!!')

'''here myfirst is function and second is a variable which is pointing towards function'''