# Multilevel Inheritance
class Human:
    def __init__(self,gender):
        self.gender=gender
    def show(self):
        print(f"I am human and my gender is  {self.gender}")
class Employee(Human):
    def __init__(self,name,company):
        Human.__init__(self,gender="Male")
        self.name=name
        self.company=company
    def show(self):
        print(f"My name is {self.name} ,I am currently working in {self.company}")
        super().show()
class Programmer(Employee):
    def __init__(self,name,role):
        Employee.__init__(self,name,company="Apple")
        self.role=role
    def show(self):
        print(f"Position : {self.role}")
        super().show()
pro=Programmer("Saurabh Chorge","Software Developer")
pro.show()