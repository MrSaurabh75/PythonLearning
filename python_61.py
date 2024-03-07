# Inheritance : It is a process in which child class aquires all the properties of parent class is known as inheritance.
 
class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def showData(self):
        print(f"Employee Name is {self.name} and id is {self.id}")
class Department(Employee):
    def showDept(self,num):
        if num==1:
            print("BackEnd Developer")
        elif num==2: 
            print("Tester") 
        else:
           print("FrontEnd Developer") 

emp = Department(45,"Saurabh")
emp.showData()
user=int(input("Enter your department code :"))
emp.showDept(user)
