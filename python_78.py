# Single Inheritance
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def makesound(self):
        print("Sound Made by the animal")
class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed=breed
    def makesound(self):
        print("Barks....")
class Cat(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Cat")
        self.breed = breed
    def makesound(self):
        print("Meow Meow")
d = Dog("Rocky","Jerman Shefered")
d.makesound()
c = Cat("Princes","Leo")
c.makesound()
a = Animal("Rocky","Jerman Shefered")
a.makesound()