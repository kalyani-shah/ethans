import sqlite3
try:
    db=sqlite3.connect('Employee')
    mycursor=db.cursor()
    data=[(311, 'Amit', 'IT', 70000), (329, 'Aditya', 'Admin', 70000),
       (591, 'Advika', 'HR', 60000)]
    mycursor.execute('''insert into emp values
    (1660,'Harsh','HR',45000)''')
    mycursor.executemany('''insert into emp values(?,?,?,?)'''
                         ,data)

except Exception as E:
    print ('Unable to interact with db', E)
else:
    db.commit()
    print ('Data inserted  Successfully in emp')
finally:
    db.close()