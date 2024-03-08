# Instance Variable vs Class Variable : Class variables are decleard at class level and instance variable are decleard at instance level

class Employee:
    company="Apple" #Class variable
    def __init__(self,name):
        self.name=name
        self.salary=13000 #Instance Variable
    def showDetail(self):
        print(f"Company name : {self.company} and salary is {self.salary}")
emp1=Employee("Saurabh")
emp1.showDetail()
emp2=Employee("Mahesh")
emp2.company="Google"
emp2.salary=20000
emp2.showDetail()