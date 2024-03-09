# dir : dir() function returns a list of all the attributes and methods.
x = [1,2,3,4]
print(dir(x))


# dict : __dict__ attribute returns a dictionary reprresentatiion of an attributes.
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"Name : {self.name} and Age : {self.age}")
s = Employee("Saurabh",21)
s.show()
print(s.__dict__)

# help : help() is a function is used to get help documentation for an object including of its attributes and methods

print(help(str))