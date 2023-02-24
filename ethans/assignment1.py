
#Core Objects:
#WAP to swap values of two integer variables without using third variable

a=20
b=40
a=a*b
b=a/b 
a=a/20
print('value of a:',a)#40
print('value of b:',b)#20


#Slicing:
#WAP to print last 3 characters of a string(regular order)

name='KALYANI'
print('last 3 char in reg order:',name[4:])

#WAP to print last 3 characters of a string(reverse order)

print('last 3 char in reverse:',name[-1:-4:-1])

#WAP to print a string except last 3 characters(fwd order)

print('except last 3 in frwd:',name[:4])

#WAP to print a string except last 3 characters(reverse order)

print('except last 3 in reverse:',name[-4::-1])

#WAP to reverse a string -

print('reverse of string:',name[::-1])

#Take an index and element from user and change the element at index in hardcoded list

l1=[1,2,3,4,5]
l1[3]=input('enter the element:')
print(l1)


#Conditional Statements :
#Python Program to Check if a Number is Positive, Negative or Zero

num=int(input('enter a num:'))
if num>0:
    print('num is positive')
elif num<0:
    print('num is negative')
else:
    print('num is zero')

#Python Program to Check if a Number is Odd or Even -

num=int(input('enter a num:'))
if num%2==0:
    print('EVEN')
else:
    print('ODD')

#Python program to check given string is Palindrome or not-

name=input('enter a name:')
if name==name[::-1]:
    print('it is a palindrome')
else:
    print('it is not')

#Python Program to Check Leap Year -

year=int(input('enter year:'))
if year%4==0:
    if year%100 !=0:
        print('year is a leap year')
    elif year%400 ==0:
        print('year is a leap year')
    else:
        print('year is not a leap year')
else:
    print('year is not a leap year')

#WAP to take a key from user and print its value if it is present in a dictionary -

d1={1:1,2:5,3:6,5:7}
num=int(input('enter a key:'))
print('value of key if present in dict:',d1[num])

#-WAP to Create a student structure with Name, Roll, Marks (English , Maths)
#add Scholarship based on student's maths marks
If Maths marks more than 70 --> 2000 Rs
			   between 60-70 -->1500 Rs
			   between 40-60 -->1000 Rs
			   less than 40  --> 0 Rs


d1={}
roll=int(input('enter student roll num:'))
d1[roll]={}
d1[roll]['name']=input('enter student name:')
d1[roll]['marks']={}
d1[roll]['marks']['M']=int(input('enter maths marks:'))
d1[roll]['marks']['E']=int(input('enter english marks:'))
if d1[roll]['marks']['M']>70 and d1[roll]['marks']['M'] <=100:
    print('scholarship is :',2000)
elif d1[roll]['marks']['M'] >=60 and d1[roll]['marks']['M'] <=70:
    print('scholarship is:',1500)
elif d1[roll]['marks']['M'] >=40 and d1[roll]['marks']['M'] <60:
    print('scholarship is:',1000)
elif d1[roll]['marks']['M'] <40 and d1[roll]['marks']['M']>0:
    print('scholarship is:',0)
else:
    print('invalid input')
 

#Write a Python program to sum all the items in a list -

l1=[22,33,44,55,66,77,88]
i=0
mysum=0
while i < len(l1):
    mysum=mysum+l1[i]
    i=i+1
print('summation:',mysum)


#Write a program to find out maximum number in the list-

l1=[22,44,55,66,88,100,200]
print('maximum number is list is:',max(l1))

#Write a program to calculate factorial if num=5 , fact is 120 (5*4*3*2*1)-

num=5
fact=1
i=1
while i<=num:
    fact=fact*i
    i=i+1
print('fact of num is:',fact)


#-Input : 
#[('G', 'E', 'E', 'K', 'S'), ('G', 'E', 'E', 'K', 'S'), ('G', 'E', 'E', 'K', 'SKKKKK')]
#Output : String --> 'GEEKSGEEKSGEEKSKKKKK'

#-WAP to get the factorial of user defined number -

num=int(input('enter a number:'))
fact=1
i=1
while i<=num:
    fact=fact*i
    i=i+1
print('factorial of number is:',fact)

#WAP to get the count of words in the statement string and 
#the count of vowels in complete statement.

name = 'python is an easy language'
print(len(name))






