# Write a program to create the class and object
# class Car:
#     def horn(self):
#         print("Horn Ok Please")
# c = Car()
# c.horn()

# Write a program to create the constructor
# class Sum:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         print(f"Addition of {self.a} and {self.b} is {self.a+self.b}")
# s = Sum(45,90)
# s.add()

# Create the class rectangle and pass the data to calculate area of rectangle
class Rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        return self.l*self.w
r = Rectangle(5,7)
result = r.area()
print(f"Area of rectangle = {result}")
