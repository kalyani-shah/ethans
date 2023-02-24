#own criteria of exception
count =0
while count <=5:
    try:
        num=int(input('enter a number:'))
        if num<=2:
            raise ValueError('please enter number >2') #here we are defining our own exception
        print('100 divided by',num,'is',100/num)
        #print ('100 divided by {} is {}' -> format(num,100/num))
        break
    except ValueError as abc:
        print('ERROR:',abc)
        count+=1
else:
    print('you have exhausted the limit')
