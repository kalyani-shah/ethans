from itertools import groupby
l1=[1,2,2,3,4,4,4,5,2,6,6,7,8]
for each in groupby(l1):
    print(each[0])
print(list(each[0] for each in groupby(l1)))

#this program deletes all consecutive duplicates.