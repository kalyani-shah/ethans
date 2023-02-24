#USER DEFINED FUNCTIONS -

def greet(): #definition of function
    print('good morning')
    print('good night')
for each in range(10):
    greet()   #calling a function


#sum of a and b using def and return function -

def mysum(a,b):
    return a+b
print (mysum(9,10))

def mysum(a,b):
    return a+b
print(mysum('abc','pqr'))


#ONLY RETURNS OUTPUT OF FIRST RETURN,OTHER RETURNS BECOME USELESS -

def myop(a,b):
    return a+b,a-b,a/b,a*b #writing in 1 line gives output in form of tuple.
    return a-b
    return a/b
    return a*b
print(myop(9,10))


#FACTORIAL OF A NUMBER -

def fact(num):
    res=1
    for each in range(2,num+1):
        res=res*each
    return res

for each in range(1,10):
    print('factorial of',each, 'is:',fact(each))


#RETURN MAXIMUM OF LIST =

def mymax(a):
    res=a[0]
    for each in a:
        if each>res:
            res=each
    return res

print(mymax([2,4,77,8]))



#FUNCTION TO FORM DICTIONARY FROM 2 LISTS {KEYS AND VALUES} WITH CONDITIONS AS=>

#IF L1 AMD L2 ARE HAVING DIFF LENGTHS,RETURN ERROR 'DIFF LENGTHS'
#IF L1 HAS ANY DUPLICATE KEYS, RETURN ERROR 'DUPLICATE KEYS'
#ELSE RETURN DICTIONARY WITH KEYS FROM L1 AND VALUES FROM L2


def hello(c,d):
    if len(c)!=len(d):
        return 'ERROR : different lengths'
    elif sorted(c)!=sorted(set(c)):
        return 'ERROR : duplicate keys'
    else:
        return dict(zip(c,d)) #DICT(ZIP) RETURNS OUTPUT IN FORM OF DICTIONARY.

print(hello([1,2,3,4,4],['a','b','c','d','e']))

---------------------------------------------------------------------------------
--------------------------------------------------------------------------------

#GENERATOR FUNCTION -

#WITHOUT USING RETURN IF WANT AN OUTPUT THEN WE USE 'YIELD' FUCNTION. THE MOMENT YOU USE YIELD IT BECOMES GENERATOR FUNCTION.

def sqlist(*a):
    for each in a:
        yield each**2
g=sqlist(5,6,7)
print(list(g))

#IN ORDER TO GET OUTPUT 2 OPTIONS ARE THERE -1] CONVERTING 'G' TO LIST.
# 2] ITERATING OVER 'G'
'''for each in g:
        print(each)
        '''


----------------------------------------------------------------------------------
-------------------------------------------------------------------------------

#MAP FUNCTION PROGRAM TO PRINT A TO Z -

a = list(map(chr,range(65,91)))
print ('alphabets list is:',a)

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------

#LAMBDA FUNCTION -

#It is an anonymous function which can be used as an argument in other function.
#gives output in one line itself.

def sq(num):
	return num**2

#So instead of defining function, below lambda function is used -

list(map(lambda x:x**2,[1,2,3,4]))
O/P --> [1, 4, 9, 16]

#MULTIPLE ARGUMENT EXAMPLE -

list(map(lambda x,y:x+y,[1,2,3],[4,5]))
[5, 7]

list(map(lambda x,y:x+y,[1,2,3],[4,5,6]))
[5, 7, 9]

---------------------------------------------------------------------------

#WRITE A PROGRAM TO CONVERT LIST TO AN INTEGER-

l1=[11,22,33]

int(''.join(map(str,l1)))
#112233 --> O/P












