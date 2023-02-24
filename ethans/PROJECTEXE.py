d1={}
while True :
    print('''select an operation to be performed from below:
          1: Add Student
          2: Remove Student
          3: Search Student
          4: exit''')
    
    a=int(input('enter operation number to be performed :'))

    if a==1:
        b=int(input('how many number of students to be added :'))
        i=1
        while i<=b:
            roll = int(input('enter student roll id :'))
            d1[roll]={}
            d1[roll]['name'] = input('enter student name :')
            d1[roll]['marks'] ={}
            d1[roll]['marks']['E']=int(input('enter students english marks :'))
            i=i+1
        print(d1)


    elif a==2:
        number=int(input('enter student roll id to be deleted : '))
        if number in d1:
            d1.pop(number)
            print('database after deleting becomes:',d1)
        else:
            print('Number does not exists in database, !! ENTER CORRECT NUMBER !!')
       
            

    elif a==3:
        d=int(input('enter roll id to be searched :'))
        for each in d1:
            if each == d:
                print('student is present in database:',d1[d])
            else:
                print('Roll number does not exists in database, ## ADD DETAILS OF STUDENT ##')

    elif a==4:
        print('thanks for using datasheet')
        break

    else:
        print('enter correct number')




   

            
        


