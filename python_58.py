# Construtor : 
class Employee:
    def __init__(self,id,name):   #__init__ is a method that help us to bulid a constructor
        self.id=id
        self.name=name
    def printName(self):
        print("Hello Mr."+(self.name)+" Your id is ",self.id)

emp = Employee(45,"Saurabh")
emp.printName()

# Write a Program to calculate the area of circle
class Circle:
    def __init__(self,r):
        self.r=r
    def Area(self):
        print(f"Area Of Circle whose radius is {self.r} are {2*3.14*self.r*self.r}")

radius = int(input("Enter radius of a Circle : "))
c = Circle(radius)
c.Area()
