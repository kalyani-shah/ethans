import sqlite3
try:
    db=sqlite3.connect('Employee')
    #db.text_factory
    cursor=db.cursor()
    cursor.execute("select * from emp")
    #print(cursor.fetchall())  -> this fetches all data in form of list
    #print(cursor.fetchone()) -> this feches only first data of an individual
   # print(cursor.fetchmany(3))  -> this fetches first 3 data from emp
    for each in cursor :
        print(each)
except Exception as E:
    print ('Unable to interact with db', E)
else:
    db.close()
    print ('Data fetched  Successfully in emp')