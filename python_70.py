# Class Methods as a alternative constructor : 
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromstr(cls,str):
        return cls(string.split("-")[0],string.split("-")[1])
e = Employee("Saurabh",15000)
print(e.name)
print(e.salary)
string = "Saurabh-25000"
e2= Employee.fromstr(string)
print(e2.name)
print(e2.salary)