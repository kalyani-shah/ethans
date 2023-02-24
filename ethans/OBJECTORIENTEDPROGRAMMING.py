#HERE IN OOP YOU DEFINE CLASS AND THEN CREATE MULTIPLE OBJECTS. LIKE IN EXAMPLE -

#FOR A CAR MANUFACTURER -

#BLUE-PRINT --> CLASS
'''BLUE-PRINT MEANS A STD DATA WHICH CONSISTS OF ALL THE DETAILS OF CAR.
   LIKE CAR ATTRIBUTES --> TYRE,ENGINE,STEERING,BRAKE
        CAR BEHAVIOUR  --> TO RUN'''
#INSTANCE OF CLASS --> OBJECT
'''INSTANCE OF CLASS MEANS WITH HELP OF BLUEPRINT ONE CAN MAKE MULTIPLE CARS'''

#PROGRAM -

class Student: #class
    def __init__(self,groll,gname):
        self.roll=groll
        self.name=gname
    def details(self):
        print('roll',self.roll)
        print('name',self.name)
s1=Student(101,'jatin')#calling class as function that time __init__ will be called as function.
#here s1 --> self, 101 --> groll, jatin --> gname
s2=Student(102,'mayank')
print(s1.name)
print(s2.details())

=================================================================================================================================
#CLASS VARIABLES AND OBJECT VARIABLES -

class Student:
	count=0
	nation='India'
	def __init__(self,groll,gname):
		self.roll=groll
		self.name=gname
		Student.count=Student.count+1
	def details(self):
		print('roll:',self.roll)
		print('name:',self.name)
		print('country:',self.nation)

		
s1=Student(101,'kalyani')
dir(s1)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
 '__str__', '__subclasshook__', '__weakref__', 'count', 'details', 'name', 'nation', 'roll']

#SO HERE S1 HAS ACCESS OF COUNT,DETAILS,NATION,NAME,ROLL

#USE OF GETATTR AND SETATTR IN ORDER TO CHANGE OBJECT NAME OR ROLL -

>>> s1.name
'kalyani'
>>> s1.name='dharmik'
>>> s1.name
'dharmik'
>>> getattr(s1,'name')
'dharmik'
>>> setattr(s1,'name','kalyani')
>>> getattr(s1,'name')
'kalyani'

#HOW MANY ATTRIBUTES AN OBJECT HAS CAN BE VIEWED BY USING -

>>> s1.__dict__
{'roll': 101, 'name': 'kalyani'}


#COUNT AND NATION SPECIFICATION -

>>> s1.count
1
>>> s2=Student(102,'mayank')
>>> s2.count
2
>>> s1.count
2
>>> s3=Student(102,'ox')
>>> s3.count
3
>>> s1.count
3
>>> s2.count
3

>>> s1.nation='china'
>>> s1.nation
'china'
>>> s2.nation
'India'
>>> s3.nation
'India'


====================================================================================================================================================

#DECORATORS -













