#COMPREHENSION -

#USING COMPREHENSION FUNCTION TO PRINT A TO Z IN LIST -
a=[chr(x) for x in range(65,91)]
print(a)

b=[x**2 for x in range(1,5)]
print(b)

c=[x**2 for x in range(1,10) if x%2 == 0]
print(c)

d=[x**2 if x%2==0 else x**3 for x in range(1,15)]
print(d)


#WAP TO PRINT OUTPUT FROM A STRING WHOSE NUMBER ARE DIVISIBLE BY 5 -

stmt = '0100,0011,1010,1100,1001,0101'
stmt.split(',')
e = [x for x in stmt.split(',') if int(x,2)%5 == 0] #UNJOIN OUTPUT
f = ''.join([x for x in stmt.split(',') if int(x,2)%5 == 0]) #JOINING OUTPUT
print(e , f)

#SET COMPREHENSION - [GIVES UNIQUE VALUE IN FORM OF SET WHEN USED '{}']

#THE MOMENT '[]' IS CONVERTED TO '{}'; WE GET AN OUTPUT IN FORM OF SET. EXAMPLE -

d={x**2 if x%2==0 else x**3 for x in range(1,15)}
print(d)

#'()' --> GIVES GENERATOR VALUE -

d=list(x**2 if x%2==0 else x**3 for x in range(1,15))
print(d)

'''
DIFFERENCE BETWEEN COMPREHENSION AND SET COMPREHENSION -

l1=[1,2,3,3,4,5]

[x**2 for x in l1]
[1, 4, 9, 9, 16, 25]

{x**2 for x in l1}
{1, 4, 9, 16, 25}
'''

#DICTIONARY OUTPUT USING COMPREHENSION -

l1=[1,2,3,4]
{x**2:x**3 for x in l1}
#OUPUT --> {1: 1, 4: 8, 9: 27, 16: 64}


#WAP TO  PRINT {1:'A',2:'B',...}

c={x-64:chr(x) for x in range(65,91)}
print(c)

#WAP TO PRINT OUTPUT {'python':6,'is':2,..}

data = 'python is very easy language'
d = {x:len(x) for x in data.split()}
print(d)


---------------------------------------------------------
----------------------------------------------------------------


#MODULAR FUNCTIONS -

RANDOM MODULE [GIVES OUTPUT IN BETWEEN 0 TO 1 ONLY]

import random

random.random()
#0.38593319024485073
for each in range(10):
    print(random.random())
#OUTPUT
0.8463003563248126
0.6829130293299737
0.3799018105870545
0.31827156919569277
0.23144381005041192
0.07997845628948885
0.8223832255725347
0.9907469425130322
0.7572277265539729
0.7527331996249068


#IF WANT IN INTEGER FORMAT -

random.randint(35,76)
63
random.randint(35,76)
66
random.randint(35,76)
70

for each in range(10):
   print(random.randint(35,76))
#OUTPUT
62
62
73
43
49
60
67
69
68
75

#RANDOMLY GIVES 35 NUMBERS ANY IN RANGE 1 TO 100 AND NONE OF NUMBER IS REPEATED ANYTIME.

random.sample(range(1,101), 35)
[28, 59, 43, 61, 56, 71, 39, 57, 55, 22, 17, 23, 78, 86, 54, 67, 42, 76, 24, 69, 81, 85, 11, 33, 20, 34, 77, 60, 87, 58, 38, 92, 94, 31, 47]
random.sample(range(1,101), 35)
[83, 5, 80, 19, 92, 48, 27, 21, 16, 28, 2, 11, 84, 8, 82, 49, 32, 24, 67, 59, 77, 66, 99, 68, 1, 94, 38, 96, 53, 47, 33, 44, 69, 81, 78]
random.sample(range(1,101), 35)
[90, 41, 68, 72, 36, 100, 26, 1, 8, 58, 12, 32, 82, 14, 46, 60, 15, 44, 87, 38, 47, 3, 25, 5, 17, 4, 45, 49, 93, 30, 71, 7, 24, 53, 85]


























