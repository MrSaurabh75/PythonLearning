# Multiple Inheritance
class Apple:
    def __init__(self,name,role1):
        self.name=name
        self.role1=role1
    def show1(self):
        print(f"My Name is {self.name} and working in Apple PVT.LTD having position {self.role1}")
class Tesla:
    def __init__(self,name,role2):
        self.name=name
        self.role2=role2
    def show2(self):
        print(f"My Name is {self.name} and working in Tesla PVT.LTD having position {self.role2}")
class CommmanEmployee(Apple,Tesla):
    def __init__(self,name):
        Apple.__init__(self,name,role1="Developer")
        Tesla.__init__(self,name,role2="UX Designer")
    def show(self):
        super().show1()
        super().show2()

emp = CommmanEmployee("Saurabh")
emp.show()