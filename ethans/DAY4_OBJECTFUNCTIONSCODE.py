#object function programs -

s1='eTHANs'
print('lower version:',s1.lower())
l1=[1,2,3]
print('newlist:',l1.append(4))


s1='eTHANs'
print('lower version:',s1.lower())
l1=[1,2,3]
l1.append(4)
print('newlist:',l1)

l1=[1,2,3,4]
sqlist=[] #want square of l1 in sqlist
for each in l1:
    sqlist.append(each**2)
print(sqlist)



#FORM A DICTIONARY WHERE;
#1 to 26 as keys and a to z as value -
#{1:'a',2:'b'} --> like these should be output. 

res={}
for each in range(65,91):
    res[each-64]=chr(each)
print(res)


#a='listen' b='silent'
#number of characters same called anagrams.

a=input('enter a name:')
b=input('enter a name:')
if sorted(a)==sorted(b):
    print('anagram')
else:
    print('it is not')
