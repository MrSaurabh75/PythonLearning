# Class Methods :Using class methodswe can change class variables directly 
class Employee:
    com="Apple"
    def show(self):
        print(f"Employee name is {self.name} and company is {self.com}")
    @classmethod
    def changeCom(self,change):
        self.com=change

e = Employee()
e.name="Saurabh"
e.show()
e.changeCom("Tesla")
e.show()
print(Employee.com)