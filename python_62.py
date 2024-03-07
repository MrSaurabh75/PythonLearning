# Access Modifiers :
class Emp:
    def __init__(self):
        self.__name="Saurabh"
    def printName(self):
        print(f"My name is {self.__name}")

ob = Emp()
print(ob._Emp__name)
ob.printName()