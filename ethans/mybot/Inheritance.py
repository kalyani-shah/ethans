from classvsobj_method import Employee
class Programmer(Employee):
    def __init__(self,getname,getsal,getproject):
        Employee.__init__(self,getname,getsal) #calling from main employee class
        self.project=getproject
    def displayEmployee(self):  #method overriding
        Employee.displayEmployee(self)
        print("project:",self.project)
class Manager(Employee):
    pass  #if for a block code not sure,rather then writing nothing we can write "pass"
if __name__=='__main__':
    p1=Programmer('jatin',50000,'TMO')
    e1=Employee('amit')
    m1=Manager('pradeep')
    p1.displayEmployee()
    print('@@@@@@@@@@@')
    m1.displayEmployee()
    Manager.displayCount()
    #print(Employee.empCount)