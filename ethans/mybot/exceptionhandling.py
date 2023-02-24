num=int(input('enter a number:'))
try:
    print('hi')
    l1=[11,2,3,4,5,66,7]
    index=int(input('enter index:'))
    print(l1[index])
    print('before zero division testing')
    print(1/num)
    print('good morning')
except Exception as E:
    print(E)
else:
    print('no exception occurred')
finally:
    print('cleanup process')

#exception -> try -> except -> finally
#no exception -> try -> else -> finally