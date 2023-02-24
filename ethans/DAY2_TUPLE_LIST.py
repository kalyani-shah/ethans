#PRACTISE -

#TUPLE,LIST,SET --> TUPLES LAST 2 ELEMENTS, LIST REVERSE, SET AS IT IS.
'''

l1=[20,'Einstein','Scientist']
print('reverse of list:',l1[::-1])
t1=(20,'Newton','Maths')
print('last 2 elements:',t1[:-3:-1])
s1={1,1,1,2,3,5,5,6}
print(s1)

#Nesting -

l1=[11,22,3,{'ID':101,'name':'Amit','Marks':{'M':65,'E':87}},77,88]
print(l1[3]['Marks']['E'])
print(l1[4])
print(l1[3]['name'])
print('l1:',l1[::-1])
print(l1[-3]['Marks']['M'])


d1={101:{'name':'amit','Marks':{'M':87,'E':92}}}
print('details',d1)


#enter user input -

a=int(input('enter value of a:'))
b=float(input('enter value of b:'))
print('sum of a & b:', a+b)

#user output-

a=int(input('enter value of a:'))
b=float(input('enter value of b:'))
print('sum of',a, '&', b,':', a+b)

#REMOVING DATA FROM PROGRAM-

#d1={101:{ 'name': 'Amit', 'Marks': {'M': 65, 'E': 87}},102:{ 'name': 'Mayank', 'Marks': {'M': 72, 'E': 24}}}

d1={}
roll = int(input('enter a roll number:'))
d1[roll]={}
d1[roll]['name']=input('enter name:')
d1[roll]['marks']={}
d1[roll]['marks']['M']=int(input('enter maths marks:'))
d1[roll]['marks']['E']=int(input('enter english marks:'))
roll = int(input('enter a roll number:'))
d1[roll]={}
d1[roll]['name']=input('enter name:')
d1[roll]['marks']={}
d1[roll]['marks']['M']=int(input('enter maths marks:'))
d1[roll]['marks']['E']=int(input('enter english marks:'))
print('details:',d1)


#num is positive or negative-

num=int(input('enter a number:'))
if num>0:
    print('num is positive')
elif num<0:
    print('num is negative')
else:
    print('num is zero')

#num is even or odd-

num=int(input('enter a num:'))
if num%2==0:
    print('even')
else:
    print('odd')

#name is palindrome or not -

name=input('enter name:')
if name==name[::-1]:
    print('palindrome')
else:
    print('not')


#if want same output multiple times-

d1={}
i=1
while i<=3:
 roll=int(input('enter roll numb:'))
 d1[roll]={}
 d1[roll]['name']=input('enter name:')
 d1[roll]['marks']={}
 d1[roll]['marks']['M']=int(input('enter maths marks:'))
 d1[roll]['marks']['E']=int(input('enter english marks:'))
 i=i+1
print('details',d1)
'''

#program for even num square and odd num cube

i=1
while i<=25:
    if i%2==0:
        print('square of num:',i**2)
    
    else:
        print('cube of num:',i**3)
    i=i+1


#print('sum of list:'sum(l1))

l1=[44,44,55,66,7,8,9,55,7]
i=0
mysum=0
while i<len(l1):
    mysum=mysum + l1[i]
    i=i+1
print('sum:',mysum)
    

