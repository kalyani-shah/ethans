#OBJECT FUNCTIONS -

#objects --> str, float, type ,print, dictionary, list, tuple, len. This all objects have specified functions.

#how to view its function ==> dir(object)

#STR FUNCTION -
----------------------------------------------------------------
------------------------------------------------------------

name='eTHANs'

dir(name)

help(name.capitalize) #signifies what an object function will throw as output.
Help on built-in function capitalize:

capitalize() method of builtins.str instance
    Return a capitalized version of the string.
    
    More specifically, make the first character have upper case and the rest lower
    case.

#name.capitalize()
'Ethans'

#name.lower()
'ethans'

#name.upper()
'ETHANS'

#name.center(10,'@')
'@@eTHANs@@'

--------------------------
name = 'aabcaadefaaa'
----------------------
#name.count('a')
7
#name.count('aa')
3
#name.count('aaa')
1

#name.index('d')
6
#name.index('a')
0

----------------------------------------------------
name='a#b#c#d'

#name.split('#')
['a', 'b', 'c', 'd']
#name.split('c#')
['a#b#', 'd']

------------------------------------------------------------------
#WHEN NO CRITERIA GIVEN TO SPLIT, IT SPLITS ON BASIS OF SPACE -

stmt='python is easy language'
#stmt.split()
['python', 'is', 'easy', 'language']

#len(stmt.split())
4

----------------------------------------------------------------------------

#JOIN ALWAYS NEEDS LIST OF STRINGS, EXAMPLE AS BELOW -

l1=['a','b','c','d']
#   '#'.join()l1'
    'a#b#c#d'

#'xyZ'.join(l1)
'axyZbxyZcxyZd'

#IF NOTHING MENTIONED GIVES JOINT WORDS -

#  ''.join(l1)
   'abcd'

------------------------------------------------------------
-----------------------------------------------------------------


#TUPLE -

t1=(33,44,33,77,88,9)
>>> dir(t1)
[ 'count', 'index']

#t1.index(77)
3
#t1.count(33)
2

----------------------------------------------------------------------------
-----------------------------------------------------------------------------------

#LIST -

l1=[11,22,33,44]
dir(l1)
[append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#APPEND KEEPS ON ADDING ELEMENT IN IT. BUT ALWAYS REMEMBER THAT L1.APPEND() THROWS NONE AS OUTPUT IN A PROGRAM.

#l1.append(66)
#l1
[11, 22, 33, 44, 66]
#l1.append((4,5))
#l1
[11, 22, 33, 44, 66, (4, 5)]


#EXAMPLE -

s1='eTHANs'
print('lower version:',s1.lower())
l1=[1,2,3]
print('newlist:',l1.append(4))

#output will be -
lower version: ethans
newlist: None


#IF WANT OUTPUT HERE -

s1='eTHANs'
print('lower version:',s1.lower())
l1=[1,2,3]
l1.append(4)
print('newlist:',l1)

#now output will be -
lower version: ethans
newlist: [1, 2, 3, 4]

-------------------------------------------------------------------------------------------------
#l1=[1,2,5,6]
#l1.clear()
l1
[] #clears the complete list.

#DIFFERENCE BETWEEN APPEND AND EXTEND. APPEND ADDS IN GROUP WHEREAS EXTEND ADDS SEPARATELY.
 
l1=[11,33,44]
#l1.append((5,6))
[11, 33, 44, (5, 6)]

#l1.extend((8,9))
[11, 33, 44, (5, 6), 8, 9]

#l1.append('ethans')
[11, 33, 44, (5, 6), 8, 9, 'ethans']

#l1.extend('ethans')
[11, 33, 44, (5, 6), 8, 9, 'ethans', 'e', 't', 'h', 'a', 'n', 's']

-----------------------------------------------------------------------------------------

#INSERT FUNCTION-
 
#l1=[1,2,3,4,5]
#l1.insert(5,9)
[1, 2, 3, 4, 5, 9]

#l1.insert(3,7)  -->ON 3RD POSITION IT ENTERS NUMBER 7 ....MEANING OF INSERT FUNCTION IN LIST.
[1, 2, 3, 7, 4, 5, 9]

---------------------------------------------------------------------------------

#COPY -

#l1=[9,10,11]
l2=l1
l3=l1.copy()
l1.append(13)
l1,l2,l3
 #OUTPUT --> ([9, 10, 11, 13], [9, 10, 11, 13], [9, 10, 11])

 -------------------------------------------------------------------------------


#POP FUNCTION - [requires an index to be entered to remove an element.]

#IT REMOVES THE ELEMENT AT THAT INDEX AND RETURNS AN OUTPUT.

 #l1=[11,22,33,44,55]

#l1.pop(2)
33
#l1.pop()
55
#l1 will become -
[11, 22, 44]

 --------------------------------------------------------------------------------

 #REMOVE FUNCTION - [requires an element number which needs to be removed.]

l1=[11,22,33,66,66,66,77] 

#l1.remove(66)
[11, 22, 33, 66, 66, 77]

#l1.remove(66)
 [11, 22, 33, 66, 77]

------------------------------------------------------------------------------

#REVERSE FUNCTION -
#[reverses the list.]

#l1=[1,2,3,4,5]
l1.reverse()
[5, 4, 3, 2, 1]

--------------------------------------------------------------------------------

#SORT FUNCTION -

l1=[33,22,66,44,2,4,3]
#l1.sort()
[2, 3, 4, 22, 33, 44, 66] # prints in ascending order by changing original list permanently.

#l1.sort(reverse = True)
[66, 44, 33, 22, 4, 3, 2] #prints in descending order.

'''DISADVANTAGE OF 'SORT' FUNCTION IS THAT IT CHANGE ORIGINAL LIST PERMANENTLY.
   SO WE HAVE A #BUILT-IN FUNCTION --->''SORTED''
   SORTED FORMS A NEW LIST WITHOUT CHANGING THE ORIGINAL LIST PERMANENTLY.
   EXAMPLE IS AS BELOW -'''


l1=[55,44,33,2,8,4]
#sorted(l1)
[2, 4, 8, 33, 44, 55]

#res=sorted(l1)
res ---> [2, 4, 8, 33, 44, 55]
l1 ---> [55, 44, 33, 2, 8, 4]


#SORTED WORKS FOR STRING AS WELL AS TUPPLE. EXAMPLES AS BELOW -


#sorted((5,2,6,4))
[2, 4, 5, 6]

#sorted('ethans')
['a', 'e', 'h', 'n', 's', 't']

 #name='sonal'
#sorted(name)
['a', 'l', 'n', 'o', 's']

 #''.join(sorted(name))
'alnos'
-------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------

#SET FUNCTIONS --

#s1={4,2,77,44,55,77}
s1 = {2, 4, 44, 77, 55}

#ADD, REMOVE, UPDATE, UNION, INTERSECTION -
 
#s1.add(88)
{2, 4, 44, 77, 55, 88}
 
#s1.remove(4)
{2, 44, 77, 55, 88}

#s1.update([55,44,3,5,6])
{2, 3, 5, 6, 44, 77, 55, 88}


#s1={1,2,3,4}
#s2={4,5,6,7}

##s1.union(s2)
{1, 2, 3, 4, 5, 6, 7}

##s1.intersection(s2)
{4}

-----------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------

#DICTIONARY FUNCTIONS -

d1 ={1:1,2:4,3:9,4:16}

#KEYS, VALUES, ITEMS -


##d1.keys()
dict_keys([1, 2, 3, 4])

'''IF WANT AN ELEMENT FROM THESE -'''

#list(d1.keys())[2]
3

 
##d1.values()
dict_values([1, 4, 9, 16])

##d1.items()
dict_items([(1, 1), (2, 4), (3, 9), (4, 16)])
-------------------------------------------------------------------------------------------------------------------------------------

#GET -

#d1.get(3)  --> enter the key value in bracket. If key is present it throws an output else if key is not present it won't throw any output.
9
#d1.get(25)
----------------------------------------------------------------------------------------------------------------------------------------------------

#d1.setdefault(25)
d1 --> {1: 1, 2: 4, 3: 9, 4: 16, 25: None}
 #So setdefault is adding the key in dictionary and throwing its value as 'None' when the key is not existing in dictionary. 


#IF KEY PRESENT THEN OUTPUT IS VALUE -

#d1.setdefault(3)
9  'VALUE AS OUTPUT'


#IF KEY-VALUE BOTH GIVEN THEN IT ADDS BOTH IN DICTIONARY. EXAMPLE -

#d1.setdefault(9,81)
81
d1 --> {1: 1, 2: 4, 3: 9, 4: 16, 25: None, 9: 81}

----------------------------------------------------------------------------------------------------------------------------------------------


#POP AND DELETE -

#d1.pop(4)
16

#del(d1[2])
d1 --> {1: 1, 3: 9, 25: None, 9: 81}


----------------------------------------------------------------------------------
 --------------------------------------------------------------------------------

 #ZIP, MAP, REDUCE, FILTER FUNCTIONS-

 1] ZIP - [FORMS PAIRING]

#zip([1,2,3,4],[5,6])
<zip object at 0x00000265D8DACB08>

#list(zip([1,2,3,4],[5,6])) CAN CONVERT TO LIST.
O/P --> [(1, 5), (2, 6)]

#dict(zip([1,2,3,4],[5,6])) CAN CONVERT TO DICTIONARY.
O/P --> {1: 5, 2: 6}


2] MAP -

[IT APPLIES FUNCTION TO EACH AND EVERY ELEMENT]

def sq(num):
	return num**2

map(sq,[1,2,3,4])
 #<map object at 0x00000265D8DBBB48>

list(map(sq,[1,2,3,4]))
#[1, 4, 9, 16] --> stored value of each element one by one and when used 'list' ; map threw the stored value in form of list.


stmt = 'kalyani is cutest girl'
list(map(len,stmt.split()))
#[7, 2, 6, 4]
stmt.split()
#['kalyani', 'is', 'cutest', 'girl']


3]REDUCE -

#GIVES ONLY ONE VALUE-

l1=[11,22,33,4,5]

from functools import reduce
reduce(lambda x,y:x+y,l1)
#75 -> OUTPUT
reduce(lambda x,y:x+y,list(l1))
#75


#USING REDUCE FUNTION TO PRINT FACTORIAL OF NUMBER -

from functools import reduce
n= int(input('enter a number:'))
print(reduce(lambda x,y:x*y,range(2,n+1)))


#USING REDUCE FUNCTION TO GET MAX OF LIST-

l1=[22,55,88,77]
from functools import reduce
reduce(lambda x,y:x if x>y else y,l1)
#88  -> OUTPUT


4] FILTER - GIVES OUTPUT OF COMPARISON WHICH IS TRUE ONLY.

#WAP TO GIVE OUTPUT OF NUMBER DIVISIBLE BY 3 FROM 1 TO 100 -

list(filter(lambda x:x%3 ==0,range(1,101)))
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

































































 


