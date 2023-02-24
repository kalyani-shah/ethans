import sqlite3  # Step1

try:
    db = sqlite3.connect('Employee')  # Step2 Connection Object
    mycursor = db.cursor()  # Step3 Creating Cursor
    mycursor.execute('''create table  if not exists emp
    (empID int NOT NULL,
    empName text,
    dept text, 
    sal int, PRIMARY KEY (empID))''')  # Step4

#table name - empID, data type -int, Constraint is - NOT NULL in case of ID

#since there is no insertion of data step 5 - commit is not there here

except Exception as E:
    print('Unable to interact with db', E)
else:
    print('Table Created Successfully')
finally:
    db.close()  # Step6
