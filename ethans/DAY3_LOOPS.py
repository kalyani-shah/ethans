#use of else in while:
#when all the iterations of while is executed AFTER THAT ONLY else iteration will execute. Example as below -

#GETTING SQ OF NUMB FROM 1 TO 10 USING WHILE ELSE LOOP -

i=1
while i<=10:
    print('square of',i,'is',i**2)
    i=i+1
else:
    print('success')


#USE OF BREAK AND CONTINUE -

#break ll stop execution once i value is 7.
i=1
while i<=10:
    if i==7:
        break
    print('square of',i,'is',i**2)
    i=i+1
else:
    print('success')


#whereas continue ll keep executing infinite times at i==7. Continue again re-directs to while.
    
i=1
while i<=10:
    if i==7:
       continue
    print('square of',i,'is',i**2)
    i=i+1
else:
    print('success')

#If I want to print all the squares except 7, then code ll be -

i=1
while i<=10:
    if i==7:
       i=i+1
       continue
    print('square of',i,'is',i**2)
    i=i+1
else:
    print('success')


#checking of number whether present or absent in list -

l1=[66,77,99,33,44]
number=int(input('enter  digit:'))
i=0
while i<len(l1):
    if l1[i]==number:
        print('present')
        break
    i=i+1
else:
    print('absent')

#FOR LOOP -

l1=[1,2,3,4]
for each in l1:
    print('square of',each,'is',each**2)

l1=[(2,4,5),(6,7),9]
#want to print sqaure of this nested list using for loop-

for each in l1:
    if type(each)==int:
        print(each**2)
    else:
        for abc in each:
            print(abc**2)

#HOW 'FOR' WORKS IN DICTIONARY -

d1={1:1,2:4,3:9}
for each in d1:
    print(each,d1[each]) #this ll print both key as well as value.

#print  inverse of above dictionary-

res={}
for each in d1:
    res[d1[each]]=each
print(res)

#print sum of a digit -

number = 123456
total = 0
for each in str(number):
    total = total + int(each)
print(total)


#If need complete output in one single line-

for each in range(1,6):
    print(each**2,end=' ')


    
