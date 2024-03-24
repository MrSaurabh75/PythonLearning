# Write a program to create the class and object
# class Car:
#     def horn(self):
#         print("Horn Ok Please")
# c = Car()
# c.horn()

# Write a program to create the constructor
class Sum:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(f"Addition of {self.a} and {self.b} is {self.a+self.b}")
s = Sum(45,90)
s.add()