# Class is a blueprint or a template for creating a onject and Object is a instance of a class that has state and behaviour

class Person:
    name = "Saurabh"
    age = 21
    salary =25000
    def info(self): #self parameter is a refrences to the current instance of a class and is used to access variables that belongs to a class
        print(f"Hello my name is {self.name}")
a = Person()
a.name="Raj"
print(a.name)
print(a.age)
print(a.salary)
a.info()