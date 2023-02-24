class Employee:
    empCount=0
    empNation='India'
    def __init__(self,getname,getsalary=20000):
       self.name=getname
       self.salary=getsalary
       Employee.empCount+=1
    def displayEmployee(self):  #object method
        print("Name :",self.name,"\nSalary:",self.salary)
        print("country :",self.empNation)
    @classmethod         #u were not ablt to call method by class
    def displayCount(self):  #class method
        print("total employee:",self.empCount)
        print("Nation :",self.empNation)
    @staticmethod        #u were not able to call a method by object
    def addNumbers(x,y):
        return x+y
if __name__ == "__main__":
    e1=Employee('gaurav',45000)
    e2=Employee('aditya')
    e2.displayCount()
    print('#############')
    Employee.displayCount()
    print(e2.addNumbers(89,11))
