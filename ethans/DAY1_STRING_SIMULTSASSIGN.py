a=100
b=200
print('sum of a+b:', a+b)
print('diff of a-b:', a-b)
print('mul of a*b:', a*b)
print('div of a/b:', a/b)

_num1=2
_num2=4
print('mul of _num1*_num2:', _num1*_num2)

c=90
d=100
c=d
trash=90
d=trash
print('value of c:',c)#100
print('value of d:',d)#90

#solved above with use of third variable.


e=50
f=90
e=e+f
f=e-f
e=e-f
print('value of e:',e)#90
print('value of f:',f)#50

#solved above w/o use of 3rd variable

#STRING

name='hello world'
print('last char:',name[-1])
print('last 3char:',name[-3:])
print('last 3 char in rev:',name[-1:-4:-1])
print('except last 3 char:',name[:-3])#hello wo
print('except last 3 in rev:',name[-4::-1])
print('reverse of string:',name[-1::-1])

